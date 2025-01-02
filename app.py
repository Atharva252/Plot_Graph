from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

# Initialize Flask app
app = Flask(__name__)

# List of disease names
disease_names = [
    'Apple__black_rot', 'Apple__healthy', 'Apple__rust', 'Apple__scab', 'Cassava__bacterial_blight',
    'Cassava__brown_streak_disease', 'Cassava__green_mottle', 'Cassava__healthy', 'Cassava__mosaic_disease',
    'Cherry__healthy', 'Cherry__powdery_mildew', 'Chili__healthy', 'Chili__leaf_curl', 'Chili__leaf_spot',
    'Chili__whitefly', 'Chili__yellowish', 'Coffee__cercospora_leaf_spot', 'Coffee__healthy', 'Coffee__red_spider_mite',
    'Coffee__rust', 'Corn__common_rust', 'Corn__gray_leaf_spot', 'Corn__healthy', 'Corn__northern_leaf_blight',
    'Cucumber__diseased', 'Cucumber__healthy', 'Gauva__diseased', 'Gauva__healthy', 'Grape__black_measles',
    'Grape__black_rot', 'Grape__healthy', 'Grape__leaf_blight_isariopsis_leaf_spot', 'Jamun__diseased', 'Jamun__healthy',
    'Lemon__diseased', 'Lemon__healthy', 'Mango__diseased', 'Mango__healthy', 'Peach__bacterial_spot', 'Peach__healthy',
    'Pepper_bell__bacterial_spot', 'Pepper_bell__healthy', 'Pomegranate__diseased', 'Pomegranate__healthy',
    'Potato__early_blight', 'Potato__healthy', 'Potato__late_blight', 'Rice__brown_spot', 'Rice__healthy', 'Rice__hispa',
    'Rice__leaf_blast', 'Rice__neck_blast', 'Soybean__bacterial_blight', 'Soybean__caterpillar',
    'Soybean__diabrotica_speciosa', 'Soybean__downy_mildew', 'Soybean__healthy', 'Soybean__mosaic_virus',
    'Soybean__powdery_mildew', 'Soybean__rust', 'Soybean__southern_blight', 'Strawberry___leaf_scorch',
    'Strawberry__healthy', 'Sugarcane__bacterial_blight', 'Sugarcane__healthy', 'Sugarcane__red_rot',
    'Sugarcane__red_stripe', 'Sugarcane__rust', 'Tea__algal_leaf', 'Tea__anthracnose', 'Tea__bird_eye_spot',
    'Tea__brown_blight', 'Tea__healthy', 'Tea__red_leaf_spot', 'Tomato__bacterial_spot', 'Tomato__early_blight',
    'Tomato__healthy', 'Tomato__late_blight', 'Tomato__leaf_mold', 'Tomato__mosaic_virus', 'Tomato__septoria_leaf_spot',
    'Tomato__spider_mites_two_spotted_spider_mite', 'Tomato__target_spot', 'Tomato__yellow_leaf_curl_virus',
    'Wheat__brown_rust', 'Wheat__healthy', 'Wheat__septoria', 'Wheat__yellow_rust'
]

# Random probabilities for each disease
disease_probabilities = np.random.rand(len(disease_names))

# Home route
@app.route('/disease-prediction', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get selected disease from the form
        selected_disease = request.form['disease_name']
        return generate_plot(selected_disease)
    return render_template('index1.html', diseases=disease_names)

# Function to generate the plot
def generate_plot(disease_name):
    if disease_name in disease_names:
        # Find the probability of the selected disease
        index = disease_names.index(disease_name)
        probability = disease_probabilities[index]
        
        # Create the plot
        plt.figure(figsize=(6, 4))
        plt.bar(disease_name, probability, color='lightgreen')
        plt.title(f'Probability of {disease_name}', fontsize=16)
        plt.xlabel('Disease', fontsize=12)
        plt.ylabel('Probability', fontsize=12)
        plt.text(0, probability + 0.01, f'{probability:.2f}', ha='center', fontsize=12)
        plt.tight_layout()
        
        # Save the plot to a buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()
        
        # Encode the plot as a base64 string
        plot_url = base64.b64encode(buf.getvalue()).decode('utf8')
        return render_template('plot.html', plot_url=plot_url)
    else:
        return f"Error: Disease '{disease_name}' is not in the list."

# Run the Flask app
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
