import gettext
import os
import base64
import time

os.system('cls' if os.name == 'nt' else 'clear')  # 清空输出
print(
    "███████╗██╗  ██╗██╗         ██████╗██╗  ██╗███████╗███╗   ██╗ ██████╗ ██████╗ ██████╗ ██████╗ \n╚══███╔╝██║  ██║██║        ██╔════╝██║  ██║██╔════╝████╗  ██║██╔════╝ ╚════██╗╚════██╗╚════██╗\n  ███╔╝ ███████║██║        ██║     ███████║█████╗  ██╔██╗ ██║██║  ███╗ █████╔╝ █████╔╝ █████╔╝\n ███╔╝  ██╔══██║██║        ██║     ██╔══██║██╔══╝  ██║╚██╗██║██║   ██║██╔═══╝  ╚═══██╗ ╚═══██╗\n███████╗██║  ██║██║███████╗╚██████╗██║  ██║███████╗██║ ╚████║╚██████╔╝███████╗██████╔╝██████╔╝\n╚══════╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═════╝ ╚═════╝ \n")
print(
    "Multimedia To HMTL\n\033[1mVersion:\033[0m 1.0.0\n\033[1mGithub:https://www.github.com/Multimedia-To-HMTL\033[0m\n\033[31mPlease visit https://www.zhicheng233.ml for more information\033[0m\n")


def convert_images_to_base64(folder_path):
    # 获取文件夹中所有图像的路径
    png_paths = []
    jpg_paths = []

    for f in os.listdir(folder_path):
        if f.endswith('.png'):
            png_paths.append(os.path.join(folder_path, f))
        elif f.endswith('.jpg'):
            jpg_paths.append(os.path.join(folder_path, f))

    # 按名称排序图像路径
    png_paths.sort()
    jpg_paths.sort()
    # 比较两个列表
    if len(png_paths) > len(jpg_paths):
        image_paths = png_paths
        image_format = "png"
    elif len(png_paths) < len(jpg_paths):
        image_paths = jpg_paths
        image_format = "jpg"
    else:
        print(_("str_id_error1"))  # png格式与jpg格式数目相同请选择要转换的格式
        imageFormatInput = int(
            input("\033[1;92m[\033[33m1\033[1;92m]\033[0mPNG\n\033[1;92m[\033[33m2\033[1;92m]\033[0mJPG\n"))
        match imageFormatInput:
            case 1:
                image_paths = png_paths
                image_format = "png"
            case 2:
                image_paths = jpg_paths
                image_format = "jpg"

    # 将每个图像转换为base64并输出
    html_data = " "
    pages = 0
    pagesTotal = len(image_paths)
    for image_path in image_paths:
        with open(image_path, 'rb') as f:
            pages = pages + 1
            image_data = f.read()
            base64_data = base64.b64encode(image_data).decode('ascii')
            html_data = html_data + "<img src=\"data:image/" + image_format + ";base64," + str(base64_data) + "\"/>\n<h1>"+str(pages)+"</h1>\n"

            os.system('cls' if os.name == 'nt' else 'clear')
            print(
                "███████╗██╗  ██╗██╗         ██████╗██╗  ██╗███████╗███╗   ██╗ ██████╗ ██████╗ ██████╗ ██████╗ \n╚══███╔╝██║  ██║██║        ██╔════╝██║  ██║██╔════╝████╗  ██║██╔════╝ ╚════██╗╚════██╗╚════██╗\n  ███╔╝ ███████║██║        ██║     ███████║█████╗  ██╔██╗ ██║██║  ███╗ █████╔╝ █████╔╝ █████╔╝\n ███╔╝  ██╔══██║██║        ██║     ██╔══██║██╔══╝  ██║╚██╗██║██║   ██║██╔═══╝  ╚═══██╗ ╚═══██╗\n███████╗██║  ██║██║███████╗╚██████╗██║  ██║███████╗██║ ╚████║╚██████╔╝███████╗██████╔╝██████╔╝\n╚══════╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═════╝ ╚═════╝ \n")
            print(
                "Multimedia To HMTL\n\033[1mVersion:\033[0m 1.0.0\n\033[1mGithub:https://www.github.com/Multimedia-To-HMTL\033[0m\n\033[31mPlease visit https://www.zhicheng233.ml for more information\033[0m\n")
            print("\033[1mPlease Wait...  ", "\033[1;92m" + str(pages), "\033[1;0m/", "\033[1;31m" + str(pagesTotal),
                "\033[1;0m - ", str(pages / pagesTotal * 100) + "%")

    with open("output.html", "w", encoding="utf-8") as f:
        f.write("<h1>技术支持&版权所有:志成zhi_cheng</h1>\n"+html_data+"<h1>Multimedia To HMTL</h1>\n<h1>Version: 1.0.0</h1>\n<h1>该程序为免费开源程序严禁任何形式倒卖  本程序遵循GPL ( GNU General Public License )开源许可协议</h1>\n<h1>Github开源仓库:https://www.github.com/Multimedia-To-HMTL</h1>\n<h1>访问 https://www.zhicheng233.ml 以获取更多内容</h1>\n<h1>捐赠吃口饭:https://www.zhicheng233.ml/Donate/</h1>\n<h1>如果你能记住我的名字，如果你们都能记住我的名字，也许我或者“我们”，终有一天能自由地生存着。</h1>\n")


langInput = int(
    input("\033[1;92m[\033[33m1\033[1;92m]\033[0m简体中文\n\033[1;92m[\033[33m2\033[1;92m]\033[0mEnglish\n"))
match langInput:
    case 1:
        es = gettext.translation('str_res', localedir='locale', languages=['zh_CN'])
        es.install()
    case 2:
        es = gettext.translation('str_res', localedir='locale', languages=['en_US'])
        es.install()
os.system('cls' if os.name == 'nt' else 'clear')  # 清空输出
print(
    "███████╗██╗  ██╗██╗         ██████╗██╗  ██╗███████╗███╗   ██╗ ██████╗ ██████╗ ██████╗ ██████╗ \n╚══███╔╝██║  ██║██║        ██╔════╝██║  ██║██╔════╝████╗  ██║██╔════╝ ╚════██╗╚════██╗╚════██╗\n  ███╔╝ ███████║██║        ██║     ███████║█████╗  ██╔██╗ ██║██║  ███╗ █████╔╝ █████╔╝ █████╔╝\n ███╔╝  ██╔══██║██║        ██║     ██╔══██║██╔══╝  ██║╚██╗██║██║   ██║██╔═══╝  ╚═══██╗ ╚═══██╗\n███████╗██║  ██║██║███████╗╚██████╗██║  ██║███████╗██║ ╚████║╚██████╔╝███████╗██████╔╝██████╔╝\n╚══════╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═════╝ ╚═════╝ \n")
print(
    "Multimedia To HMTL\n\033[1mVersion:\033[0m 1.0.0\n\033[1mGithub:https://www.github.com/Multimedia-To-HMTL\033["
    "0m\n\033[31mPlease visit https://www.zhicheng233.ml for more information\033[0m\n")
print(_("STR_ID_Welcome"))  # print("欢迎使用Multimedia To HMTL~")
print(_("STR_ID_WeiHu"))  # print("该项目由志成zhi_cheng维护")
print("\033[31m" + _("STR_ID_JiaoCheng") + "\033[0m\n")  # print("\033[31m使用前请仔细查看教程\033[0m\n")
print(_("STR_ID_ShuoMing"))  # print("该程序用于批量将多媒体文件如PNG转为Html以实现某些特殊需求")
print("\033[33m" + _("STR_ID_ShuoMing2") + "\033[0m\n")  # print("\033[33m目前仅实现图片转HTML\033[0m\n")
print("\033[1m" + _("STR_ID_MoShi") + "\033[0m\n")  # print("\033[1m请选择转换模式:\033[0m\n")
modelInput = int(input("\033[1;32m[\033[33m1\033[1;32m]\033[0m" + _("STR_ID_ImageToHTML") + "\n"))  # 图片转HTML
match modelInput:
    case 1:
        os.system('cls' if os.name == 'nt' else 'clear')  # 清空输出
        print("\033[101;93m" + _("STR_ID_ShuoMing3") + "\033[0m\n")  # print("程序会根据名称对文件进行排序，请确认文件夹内的文件命名符合规范")
        folder_path = input(_('STR_ID_LuJin') + "\n")  # 请输入文件夹路径：
        convert_images_to_base64(folder_path)

os.system('cls' if os.name == 'nt' else 'clear')  # 清空输出
print(
    "███████╗██╗  ██╗██╗         ██████╗██╗  ██╗███████╗███╗   ██╗ ██████╗ ██████╗ ██████╗ ██████╗ \n╚══███╔╝██║  ██║██║        ██╔════╝██║  ██║██╔════╝████╗  ██║██╔════╝ ╚════██╗╚════██╗╚════██╗\n  ███╔╝ ███████║██║        ██║     ███████║█████╗  ██╔██╗ ██║██║  ███╗ █████╔╝ █████╔╝ █████╔╝\n ███╔╝  ██╔══██║██║        ██║     ██╔══██║██╔══╝  ██║╚██╗██║██║   ██║██╔═══╝  ╚═══██╗ ╚═══██╗\n███████╗██║  ██║██║███████╗╚██████╗██║  ██║███████╗██║ ╚████║╚██████╔╝███████╗██████╔╝██████╔╝\n╚══════╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═════╝ ╚═════╝ \n")
print(
    "Multimedia To HMTL\n\033[1mVersion:\033[0m 1.0.0\n\033[1mGithub:https://www.github.com/Multimedia-To-HMTL\033[0m\n\033[31mPlease visit https://www.zhicheng233.ml for more information\033[0m\n")

print("\033[92m" + _("STR_ID_Done") + "\033[0m\n")  # 完成!
print("\033[1;35m如果你能记住我的名字，如果你们都能记住我的名字，也许我或者“我们”，终有一天能自由地生存着。\033[0m")
print("赞助:https://www.zhicheng233.ml/Donate/")
