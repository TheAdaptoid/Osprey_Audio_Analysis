Write-Host "Creating virtual environment..."
python -m venv .venv --clear
.venv\Scripts\Activate.ps1

Write-Host "Installing requirements..."
pip install -r requirements.txt