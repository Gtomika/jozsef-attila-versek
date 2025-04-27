import os
import shutil
import nltk


# def create_install_directory():
#
#     if not os.path.exists(install_dir):
#         os.makedirs(install_dir)
#     print(f'Created language pack installation directory: {install_dir}')


def install_hungarian_pack():
    hungarian_pack_file = os.path.join('..', 'hungarian.pickle')

    install_dir = os.path.join(os.getenv('APPDATA'), 'nltk_data', 'tokenizers', 'punkt')
    shutil.copy(hungarian_pack_file, f'{install_dir}/hungarian.pickle')
    print(f'Installed hungarian language pack to {install_dir}')

    py3_install_dir = os.path.join(os.getenv('APPDATA'), 'nltk_data', 'tokenizers', 'punkt', 'PY3')
    shutil.copy(hungarian_pack_file, f'{py3_install_dir}/hungarian.pickle')
    print(f'Installed hungarian language pack to {py3_install_dir}')


if __name__=="__main__":
    nltk.download('punkt') # downloads and installs some default language packs, creates directories
    # create_install_directory()
    install_hungarian_pack()