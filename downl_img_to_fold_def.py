def downl_img_to_fold(url, path, serial_number):
    '''Функция загружает фотографии по ссылке, полученной в качестве аргумента <url>'''
    filename = f'{path}/{serial_number}.{get_extension(url)}'
    if not os.path.exists(path):
        os.makedirs(path)
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)