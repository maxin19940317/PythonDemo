import os
import subprocess


def pdf2image(pdf_file, out_image_path=None, quality=100, dpi=300):
    params = []
    params += ["-density", str(dpi)]
    params += ["-quality", str(quality)]
    # params += ["-trim"]
    params += ["-antialias"]

    file_name, file_ext = pdf_file.split('.')
    if not file_ext == 'pdf':
        print('path is not a .pdf file.')

    if not os.path.exists(out_image_path):
        os.makedirs(out_image_path)
        print('mkdir {}'.format(out_image_path))

    args = ["convert"] + params + [pdf_file] + [os.path.join(out_image_path, '1.jpg')]
    print(args)
    subprocess.check_call(args)


def save_pdf_to_image(pdf_path, img_path):
    pdf_list = os.listdir(pdf_path)
    for pdf_file in pdf_list:
        # print(pdf_path + pdf_file)
        out_image_path = img_path + pdf_file[0:-4]
        print(out_image_path)
        pdf2image(pdf_path + pdf_file, out_image_path)


if __name__=='__main__':
    pdf_path = 'data/pdf/'
    img_path = 'data/image/'

    save_pdf_to_image(pdf_path, img_path)
    print('OK')
