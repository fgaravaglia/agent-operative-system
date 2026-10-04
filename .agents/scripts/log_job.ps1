param (
    [string]$Phase = "start"
)

# Calcola dinamicamente la root del progetto partendo dalla posizione di questo script (.agents/scripts/)
$ProjectRoot = Resolve-Path "$PSScriptRoot\..\.."
$LogsDir = Join-Path -Path $ProjectRoot -ChildPath "logs"

# Crea la cartella 'logs' nella root se non esiste già
if (-not (Test-Path -Path $LogsDir)) {
    New-Item -Path $LogsDir -ItemType Directory -Force | Out-Null
}

$LogFile = Join-Path -Path $LogsDir -ChildPath "jobs.json"
$StateFile = "$env:TEMP\antigravity_last_job.json"
$AgentId = "podcast-asset-generator"

# Legge il payload inviato da Antigravity via stdin
$InputPayload = $Input | Out-String
$PayloadData = $null
if ($InputPayload.Trim()) {
    $PayloadData = $InputPayload | ConvertFrom-Json -ErrorAction SilentlyContinue
}

# Timestamp ISO 8601 con offset fuso orario
$Now = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")

if ($Phase -eq "start") {
    $JobSuffix = (Get-Date).ToString("yyyyMMddTHHmmss")
    $JobId = "${AgentId}_${JobSuffix}"

    # Salva lo stato temporaneo per recuperare started_at e job_id alla chiusura
    $State = @{
        job_id     = $JobId
        started_at = $Now
    }
    $State | ConvertTo-Json -Compress | Set-Content -Path $StateFile -Encoding UTF8

    # Struttura evento 'running'
    $LogEntry = [ordered]@{
        job_id     = $JobId
        agent_id   = $AgentId
        status     = "running"
        started_at = $Now
        ended_at   = $null
        error      = $null
    }

    # Appende al file logs/jobs.json
    ($LogEntry | ConvertTo-Json -Compress) | Out-File -FilePath $LogFile -Append -Encoding UTF8

}
elseif ($Phase -eq "stop") {
    if (Test-Path -Path $StateFile) {
        $State = Get-Content -Path $StateFile -Raw | ConvertFrom-Json
        $JobId = $State.job_id
        $StartedAt = $State.started_at
        Remove-Item -Path $StateFile -Force -ErrorAction SilentlyContinue
    }
    else {
        $JobId = "${AgentId}_unknown"
        $StartedAt = $Now
    }

    # Verifica presenza errori dal payload di Stop
    $ErrorMsg = $null
    if ($PayloadData) {
        if ($PayloadData.error) { 
            $ErrorMsg = $PayloadData.error 
        }
        elseif ($PayloadData.stopReason -and $PayloadData.stopReason -ne "completed") { 
            $ErrorMsg = $PayloadData.stopReason 
        }
    }

    $Status = if ($ErrorMsg) { "error" } else { "success" }

    # Struttura evento 'success' o 'error'
    $LogEntry = [ordered]@{
        job_id     = $JobId
        agent_id   = $AgentId
        status     = $Status
        started_at = $StartedAt
        ended_at   = $Now
        error      = $ErrorMsg
    }

    # Appende al file logs/jobs.json
    ($LogEntry | ConvertTo-Json -Compress) | Out-File -FilePath $LogFile -Append -Encoding UTF8
}