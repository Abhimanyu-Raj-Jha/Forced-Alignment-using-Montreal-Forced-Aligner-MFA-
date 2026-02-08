# 1. ENVIRONMENT SETUP
eval "$(conda shell.bash hook)"
conda activate mfa
echo "Preparing data..."
python prepare_data.py

# 2. DOWNLOAD MODELS
echo "Downloading models..."
mfa model download acoustic english_us_arpa
mfa model download dictionary english_us_arpa
mfa model download g2p english_us_arpa

# 3. OOV HANDLING AND DICTIONARY PREPARATION
echo "Generating custom dictionary..."
mfa g2p corpus english_us_arpa custom_dict.txt --clean

# 4. RUNNING ALIGNMENT AND GENERATING TEXTGRID FILES
echo "Running alignment..."
mfa align corpus custom_dict.txt english_us_arpa output_grids --clean --beam 100 --retry_beam 400
echo "Alignment complete! Check the output_grids folder."