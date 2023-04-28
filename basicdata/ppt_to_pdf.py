import os
import subprocess
from PIL import Image
from reportlab.pdfgen import canvas


def convert_to_pdf(input_file_path, output_file_path):
    if input_file_path.lower().endswith(('.doc', '.docx')):
        # Convert doc/docx to PDF using LibreOffice command line
        cmd = 'libreoffice --headless --convert-to pdf --outdir "{}" "{}"'.format(
            os.path.dirname(output_file_path), input_file_path)
        subprocess.call(cmd, shell=True)
    elif input_file_path.lower().endswith(('.ppt', '.pptx')):
        # Convert ppt/pptx to individual PNG images using ImageMagick command line
        png_dir = os.path.join(os.path.dirname(output_file_path), 'png')
        os.makedirs(png_dir, exist_ok=True)
        cmd = 'magick convert "{}" -density 300 -quality 100 "{}/slide-%%02d.png"'.format(
            input_file_path, png_dir)
        subprocess.call(cmd, shell=True)

        # Combine PNG images into one PDF using ReportLab
        with open(output_file_path, 'wb') as pdf_file:
            canvas_obj = canvas.Canvas(pdf_file)
            for i, png_file in enumerate(sorted(os.listdir(png_dir)), start=1):
                png_path = os.path.join(png_dir, png_file)
                img = Image.open(png_path)
                canvas_obj.setPageSize(img.size)
                canvas_obj.drawImage(png_path, 0, 0, img.size[0], img.size[1])
                canvas_obj.showPage()
                img.close()
            canvas_obj.save()
    else:
        raise ValueError('Unsupported input file type')


if __name__ == '__main__':
    input_file_path = 'D:\aa\\test-lc-18612345678.pptx'
    output_file_path = 'example.pdf'
    convert_to_pdf(input_file_path, output_file_path)
