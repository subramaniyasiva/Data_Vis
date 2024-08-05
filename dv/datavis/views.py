from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import logging

logger = logging.getLogger(__name__)

def upload_file(request):
    if request.method == "POST":
        if 'excel_file' in request.FILES:
            excel_file = request.FILES["excel_file"]

            # Check if the uploaded file is a CSV file
            if not excel_file.name.endswith('.csv'):
                return render(request, "upload.html", {"error": "Uploaded file is not a CSV file."})

            try:
                # Read the CSV file into a Pandas DataFrame
                df = pd.read_csv(excel_file)
                logger.info("CSV file read successfully")
                logger.info("\n" + df.head().to_string())  # Log the first few rows of the DataFrame for debugging
            except Exception as e:
                logger.error(f"Error reading CSV file: {str(e)}")
                return render(request, "upload.html", {"error": f"Error reading CSV file: {str(e)}"})

            try:
                # Generate a chart (example: bar chart)
                plt.figure()
                df.plot(kind='bar')
                plt.title('Bar Chart')
                plt.xlabel('X-axis')
                plt.ylabel('Y-axis')
                plt.tight_layout()

                # Save the chart to a BytesIO object
                buffer = io.BytesIO()
                plt.savefig(buffer, format='png')
                buffer.seek(0)
                image_png = buffer.getvalue()
                buffer.close()

                # Encode the image to base64
                image_base64 = base64.b64encode(image_png).decode('utf-8')

                # Get DataFrame sections
                df_head = df.head().to_html()
                df_tail = df.tail().to_html()
                df_describe = df.describe().to_html()

                logger.info("Chart generated and encoded to base64 successfully")

                # Render the template with the image and DataFrame sections
                return render(request, "upload.html", {
                    "chart": image_base64,
                    "df_head": df_head,
                    "df_tail": df_tail,
                    "df_describe": df_describe
                })
            except Exception as e:
                logger.error(f"Error generating chart: {str(e)}")
                return render(request, "upload.html", {"error": f"Error generating chart: {str(e)}"})
        else:
            # Handle the case where no file is uploaded
            return render(request, "upload.html", {"error": "No file uploaded."})

    return render(request, "upload.html")
def contact_us(request):
    return render(request,"E:/django project/data vis/dv/templates/contact us.html")