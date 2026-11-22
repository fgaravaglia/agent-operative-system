# Local Tools Installation Guide

Step-by-step setup instructions for local CLI utilities and dependencies required by JARVIS scripts on Windows.

## 1. Microsoft MarkItDown (`markitdown`)

Required by `.agents/scripts/convert-to-md.ps1` to convert binary files (PDF, DOCX, PPTX, XLSX) into Markdown locally.

### Prerequisites

- Windows 10/11 with PowerShell 5.1 or PowerShell 7+.
- Python 3.10 or higher installed and added to the system `PATH`.

### Installation Steps

1. Open PowerShell and verify that Python and `pip` are accessible:

   ```powershell
   python --version
   pip --version
   ```

2. Install the `markitdown` package globally (or inside your dedicated workspace virtual environment):

   ```powershell
   python -m pip install markitdown
   python -m pip install "markitdown[pdf,docx,pptx,xlsx]"
   ```

   *(Optional)* If you need full support for all office formats and audio/OCR dependencies:

   ```powershell
   pip install "markitdown[all]"
   ```

### Verification

Run a quick check in PowerShell to confirm the CLI executable is registered in your `PATH`:

```powershell
markitdown --help
```

If the help output prints without errors, the `.agents/scripts/convert-to-md.ps1` wrapper is ready to use.
