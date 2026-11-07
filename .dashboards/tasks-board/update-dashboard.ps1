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

# Escape backticks and dollar signs for template replacement
$safeMdContent = $taskboardContent.Replace('`', '\`').Replace('$', '\$')

# Replace the INITIAL_TASKBOARD_MD content
$pattern = 'const INITIAL_TASKBOARD_MD = `[\s\S]*?`;'
$replacement = "const INITIAL_TASKBOARD_MD = `$safeMdContent`;"

if ($htmlContent -match $pattern) {
    $updatedHtml = [regex]::Replace($htmlContent, $pattern, $replacement)
    Set-Content -Path $htmlPath -Value $updatedHtml -Encoding UTF8
    Write-Host "Dashboard index.html aggiornato con successo da TaskBoard.md."
} else {
    Write-Error "Impossibile individuare il blocco INITIAL_TASKBOARD_MD in index.html."
    exit 1
}
