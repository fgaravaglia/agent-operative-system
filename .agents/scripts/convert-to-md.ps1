param(
    [Parameter(Mandatory = $true)]
    [string]$FilePath
)

if (-not (Test-Path $FilePath)) {
    Write-Error "File non trovato: $FilePath"
    exit 1
}

$outputFile = [System.IO.Path]::ChangeExtension($FilePath, ".md")

# Esegue MarkItDown via CLI Python
python -m markitdown "$FilePath" -o "$outputFile"

Write-Host "Convertito con successo: $outputFile" -ForegroundColor Green