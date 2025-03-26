echo -e "\nFormating code..."
black --check .

echo -e "\nLinting code..."
pylint --output-format=colorized osprey_audio_analysis/

echo -e "\nRunning type checking..."
mypy osprey_audio_analysis/

echo -e "\nRunning tests..."
pytest --cov=osprey_audio_analysis tests/