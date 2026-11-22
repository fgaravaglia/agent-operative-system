<#
.SYNOPSIS
  Aggiorna i dati incorporati in index.html partendo da TaskBoard.md senza invocare modelli AI.
#>

$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$vaultDir = Split-Path -Parent (Split-Path -Parent $scriptDir)
$taskboardPath = Join-Path $vaultDir "TaskBoard.md"
$htmlPath = Join-Path $scriptDir "index.html"

if (-not (Test-Path $taskboardPath)) {
    Write-Error "TaskBoard.md non trovato in: $taskboardPath"
    exit 1
}

if (-not (Test-Path $htmlPath)) {
    Write-Error "index.html non trovato in: $htmlPath"
    exit 1
}

$taskboardContent = Get-Content -Path $taskboardPath -Raw -Encoding UTF8
$htmlContent = Get-Content -Path $htmlPath -Raw -Encoding UTF8

$startTag = '<script type="text/markdown" id="initialTaskboard">'
$endTag = '</script>'

$startIndex = $htmlContent.IndexOf($startTag)
if ($startIndex -ge 0) {
    $endIndex = $htmlContent.IndexOf($endTag, $startIndex)
    if ($endIndex -gt $startIndex) {
        $prefix = $htmlContent.Substring(0, $startIndex + $startTag.Length)
        $suffix = $htmlContent.Substring($endIndex)
        $newHtml = $prefix + "`r`n" + $taskboardContent.Trim() + "`r`n  " + $suffix
        Set-Content -Path $htmlPath -Value $newHtml -Encoding UTF8
        Write-Host "Dashboard index.html aggiornato con successo da TaskBoard.md."
        exit 0
    }
}

Write-Error "Impossibile individuare il blocco <script type='text/markdown' id='initialTaskboard'> in index.html."
exit 1
