import asyncio
import threading
from asyncio import run_coroutine_threadsafe

import httpx
import requests
from mirai import Mirai, WebSocketAdapter, GroupMessage, Image, At, Startup, FriendMessage, Shutdown, Voice
import logging
import yaml
import colorlog as colorlog

import tkinter as tk
def newLogger():
    # 创建一个logger对象
    logger = logging.getLogger("selfVoice")
    # 设置日志级别为DEBUG，这样可以输出所有级别的日志
    logger.setLevel(logging.DEBUG)
    # 创建一个StreamHandler对象，用于输出日志到控制台
    console_handler = logging.StreamHandler()
    # 设置控制台输出的日志格式和颜色
    logger.propagate = False
    console_format = '%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    console_colors = {
        'DEBUG': 'white',
        'INFO': 'cyan',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
    console_formatter = colorlog.ColoredFormatter(console_format, log_colors=console_colors)
    console_handler.setFormatter(console_formatter)
    # 将控制台处理器添加到logger对象中
    logger.addHandler(console_handler)
    # 使用不同级别的方法来记录不同重要性的事件
    return logger


async def superVG(speaker,text):

    if speaker not in ["BT", "塔菲", "阿梓", "otto", "丁真", "星瞳", "东雪莲", "嘉然", "孙笑川", "亚托克斯", "文静", "鹿鸣", "奶绿", "七海", "恬豆",
                       "科比","胡桃"]:

        # os.system("where python")
        # p = random_str() + ".mp3"
        # p = "data/voices/" + p
        p = "test.wav"
        url = f"https://api.lolimi.cn/API/yyhc/y.php?msg={text}&speaker={speaker}"
        async with httpx.AsyncClient(timeout=200) as client:
            r = await client.post(url)
            newUrl = r.json().get("music")
            print("outvits语音合成路径：" + p)
            r1 = requests.get(newUrl)
            with open(p, "wb") as f:
                f.write(r1.content)
            # await change_sample_rate(p)
            return p
    else:
        with open('settings.yaml', 'r', encoding='utf-8') as f:
            resultb = yaml.load(f.read(), Loader=yaml.FullLoader)

        modelscopeCookie = resultb.get("modelscopeCookie")
        if modelscopeCookie == "":
            modelscopeCookie = "cna=j117HdPDmkoCAXjC3hh/4rjk; ajs_anonymous_id=5aa505b4-8510-47b5-a1e3-6ead158f3375; t=27c49d517b916cf11d961fa3769794dd; uuid_tt_dd=11_99759509594-1710000225471-034528; log_Id_click=16; log_Id_pv=12; log_Id_view=277; xlly_s=1; csrf_session=MTcxMzgzODI5OHxEdi1CQkFFQ180SUFBUkFCRUFBQU12LUNBQUVHYzNSeWFXNW5EQW9BQ0dOemNtWlRZV3gwQm5OMGNtbHVad3dTQUJCNFkwRTFkbXAwV0VVME0wOUliakZwfHNEIp5sKWkjeJWKw1IphSS3e4R_7GyEFoKKuDQuivUs; csrf_token=TkLyvVj3to4G5Mn_chtw3OI8rRA%3D; _samesite_flag_=true; cookie2=11ccab40999fa9943d4003d08b6167a0; _tb_token_=555ee71fdee17; _gid=GA1.2.1037864555.1713838369; h_uid=2215351576043; _xsrf=2|f9186bd2|74ae7c9a48110f4a37f600b090d68deb|1713840596; csg=242c1dff; m_session_id=769d7c25-d715-4e3f-80de-02b9dbfef325; _gat_gtag_UA_156449732_1=1; _ga_R1FN4KJKJH=GS1.1.1713838368.22.1.1713841094.0.0.0; _ga=GA1.1.884310199.1697973032; tfstk=fE4KxBD09OXHPxSuRWsgUB8pSH5GXivUTzyBrU0oKGwtCSJHK7N3ebe0Ce4n-4Y8X8wideDotbQ8C7kBE3queYwEQ6OotW08WzexZUVIaNlgVbmIN7MQBYNmR0rnEvD-y7yAstbcoWPEz26cnZfu0a_qzY_oPpRUGhg5ntbgh_D3W4ZudTQmX5MZwX9IN8ts1AlkAYwSdc9sMjuSF8g56fGrgX9SFbgs5bGWtBHkOYL8Srdy07KF-tW4Wf6rhWQBrfUt9DHbOyLWPBhKvxNIBtEfyXi_a0UyaUn8OoyrGJ9CeYzT1yZbhOxndoh8iuFCRFg38WZjVr6yVWunpVaQDQT762H3ezewpOHb85aq5cbfM5aaKWzTZQ_Ss-D_TygRlsuKRvgt_zXwRYE_VymEzp6-UPF_RuIrsr4vHFpmHbxC61Ky4DGguGhnEBxD7Zhtn1xM43oi_fHc61Ky4DGZ6xfGo3-rjf5..; isg=BKKjOsZlMNqsZy8UH4-lXjE_8ygE86YNIkwdKew665XKv0I51IGvHCUz7_tDrx6l"
        headersa = {
            "Content-Type": "application/json",
            "Origin": "https://www.modelscope.cn",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
            "Cookie": modelscopeCookie
        }
        if text == "" or text == " ":
            text = "哼哼"
        if speaker == "阿梓":
            url = "https://www.modelscope.cn/api/v1/studio/xzjosh/Azusa-Bert-VITS2-2.3/gradio/run/predict"
            newurp = "https://www.modelscope.cn/api/v1/studio/xzjosh/Azusa-Bert-VITS2-2.3/gradio/file="
        elif speaker == "otto":
            url = "https://www.modelscope.cn/api/v1/studio/xzjosh/otto-Bert-VITS2-2.3/gradio/run/predict"
            newurp = "https://www.modelscope.cn/api/v1/studio/xzjosh/otto-Bert-VITS2-2.3/gradio/file="
        elif speaker == "塔菲":
            speaker = "taffy"
            url = "https://www.modelscope.cn/api/v1/studio/xzjosh/Taffy-Bert-VITS2/gradio/run/predict"
            newurp = "https://www.modelscope.cn/api/v1/studio/xzjosh/Taffy-Bert-VITS2/gradio/file="
        elif speaker == "星瞳":
            speaker = "XingTong"
            url = "https://www.modelscope.cn/api/v1/studio/xzjosh/XingTong-Bert-VITS2/gradio/run/predict"
            newurp = "https://www.modelscope.cn/api/v1/studio/xzjosh/XingTong-Bert-VITS2/gradio/file="
        elif speaker == "丁真":
            url = "https://www.modelscope.cn/api/v1/studio/xzjosh/DZ-Bert-VITS2-2.3/gradio/run/predict"
            newurp = "https://www.modelscope.cn/api/v1/studio/xzjosh/DZ-Bert-VITS2-2.3/gradio/file="
        elif speaker == "东雪莲":
            url = "https://www.modelscope.cn/api/v1/studio/xzjosh/Azuma-Bert-VITS2-2.3/gradio/run/predict"
            newurp = "https://www.modelscope.cn/api/v1/studio/xzjosh/Azuma-Bert-VITS2-2.3/gradio/file="
        elif speaker == "嘉然":
            url = "https://www.modelscope.cn/api/v1/studio/xzjosh/Diana-Bert-VITS2-2.3/gradio/run/predict"
            newurp = "https://www.modelscope.cn/api/v1/studio/xzjosh/Diana-Bert-VITS2-2.3/gradio/file="
        elif speaker == "孙笑川":
            url = "https://www.modelscope.cn/api/v1/studio/xzjosh/SXC-Bert-VITS2/gradio/run/predict"
            newurp = "https://www.modelscope.cn/api/v1/studio/xzjosh/SXC-Bert-VITS2/gradio/file="
        elif speaker == "鹿鸣":
            speaker = "Lumi"
            url = "https://www.modelscope.cn/api/v1/studio/xzjosh/Lumi-Bert-VITS2/gradio/run/predict"
            newurp = "https://www.modelscope.cn/api/v1/studio/xzjosh/Lumi-Bert-VITS2/gradio/file="
        elif speaker == "文静":
            speaker = "Wenjing"
            url = "https://www.modelscope.cn/api/v1/studio/xzjosh/Wenjing-Bert-VITS2/gradio/run/predict"
            newurp = "https://www.modelscope.cn/api/v1/studio/xzjosh/Wenjing-Bert-VITS2/gradio/file="
        elif speaker == "亚托克斯":
            speaker = "Aatrox"
            url = "https://www.modelscope.cn/api/v1/studio/xzjosh/Aatrox-Bert-VITS2/gradio/run/predict"
            newurp = "https://www.modelscope.cn/api/v1/studio/xzjosh/Aatrox-Bert-VITS2/gradio/file="
        elif speaker == "奶绿":
            speaker = "明前奶绿"
            url = "https://www.modelscope.cn/api/v1/studio/xzjosh/LAPLACE-Bert-VITS2-2.3/gradio/run/predict"
            newurp = "https://www.modelscope.cn/api/v1/studio/xzjosh/LAPLACE-Bert-VITS2-2.3/gradio/file="
        elif speaker == "七海":
            speaker = "Nana7mi"
            url = "https://www.modelscope.cn/api/v1/studio/xzjosh/Nana7mi-Bert-VITS2/gradio/run/predict"
            newurp = "https://www.modelscope.cn/api/v1/studio/xzjosh/Nana7mi-Bert-VITS2/gradio/file="
        elif speaker == "恬豆":
            speaker = "Bekki"
            url = "https://www.modelscope.cn/api/v1/studio/xzjosh/Bekki-Bert-VITS2/gradio/run/predict"
            newurp = "https://www.modelscope.cn/api/v1/studio/xzjosh/Bekki-Bert-VITS2/gradio/file="
        elif speaker == "科比":
            url = "https://www.modelscope.cn/api/v1/studio/xzjosh/Kobe-Bert-VITS2-2.3/gradio/run/predict"
            newurp = "https://www.modelscope.cn/api/v1/studio/xzjosh/Kobe-Bert-VITS2-2.3/gradio/file="
        elif speaker=="胡桃":
            speaker="hutao"
            url = "https://www.modelscope.cn/api/v1/studio/Xzkong/AI-hutao/gradio/run/predict"
            newurp = "https://www.modelscope.cn/api/v1/studio/Xzkong/AI-hutao/gradio/file="
        data = {
            "data": [text, speaker, 0.5, 0.5, 0.9, 1, "auto", None, "Happy", "Text prompt", "", 0.7],
            "event_data": None,
            "fn_index": 0,
            "dataType": ["textbox", "dropdown", "slider", "slider", "slider", "slider", "dropdown",
                         "audio",
                         "textbox",
                         "radio", "textbox", "slider"],
            "session_hash": "xjwen214wqf"
        }
        p = "t.wav"
        async with httpx.AsyncClient(timeout=200, headers=headersa) as client:
            r = await client.post(url, json=data)
            newurl = newurp + \
                     r.json().get("data")[1].get("name")
            async with httpx.AsyncClient(timeout=200, headers=headersa) as client:
                r = await client.get(newurl)
                with open(p, "wb") as f:
                    f.write(r.content)
                return p

def main(bot,logger):
    global aimGroup
    global aimFriend
    global speaker
    @bot.on(FriendMessage)
    async def sendTo(event: FriendMessage):
        global aimGroup
        global aimFriend
        global speaker
        speaker="阿梓"
        if event.sender.id==master:
            if str(event.message_chain).startswith("连接群 "):
                aimGroup=int(str(event.message_chain).split(" ")[1])
                await bot.send(event,"设置连接成功")
            elif str(event.message_chain).startswith("连接好友 "):
                aimFriend=int(str(event.message_chain).split(" ")[1])
                await bot.send(event, "设置连接成功")
            elif str(event.message_chain).startswith("设定 "):
                speaker = str(event.message_chain).split(" ")[1]
                await bot.send(event, "设置speaker成功")
            elif str(event.message_chain).startswith("群 "):
                text=str(event.message_chain).replace("群 ","")
                p=await superVG(speaker,text)
                await bot.send_group_message(aimGroup,Voice(path=p))
                await bot.send(event, "发送成功")
            elif str(event.message_chain).startswith("好友 "):
                text=str(event.message_chain).replace("好友 ","")
                p=await superVG(speaker,text)
                await bot.send_friend_message(aimFriend,Voice(path=p))
                await bot.send(event, "发送成功")
async def vg(target_group, target_friend, speaker, text, bot):
    if target_group!="":
        p=await superVG(speaker,text)
        await bot.send_group_message(int(target_group),Voice(path=p))
    if target_friend!="":
        p=await superVG(speaker,text)
        await bot.send_friend_message(int(target_friend),Voice(path=p))
def ui(bot, logger):
    root = tk.Tk()
    root.title("输入界面")

    # 创建标签和输入框，并使用pack布局管理器进行布局
    tk.Label(root, text="目标群:").pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)
    entry_target_group = tk.Entry(root)
    entry_target_group.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

    tk.Label(root, text="目标好友:").pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)
    entry_target_friend = tk.Entry(root)
    entry_target_friend.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

    tk.Label(root, text="Speaker:").pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)
    entry_speaker = tk.Entry(root)
    entry_speaker.insert(0, "阿梓")  # 默认值为"阿梓"
    entry_speaker.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

    tk.Label(root, text="文本:").pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)
    entry_text = tk.Entry(root)
    entry_text.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

    # 创建提交按钮
    button = tk.Button(root, text="提交", command=lambda: on_button_click())
    button.pack(side=tk.TOP, pady=10)

    def on_button_click():
        # 获取输入框的内容
        target_group = entry_target_group.get()
        target_friend = entry_target_friend.get()
        speaker = entry_speaker.get()
        text = entry_text.get()
        logger.info(f"开始语音合成任务：{speaker} | {text}")
        #print(target_group, target_friend, speaker, text, bot)
        # 从另一个线程调用异步函数
        asyncio.run(vg(target_group, target_friend, speaker, text, bot))


    root.mainloop()
def run_ui_in_thread(bot, logger):
    threading.Thread(target=ui, args=(bot, logger), daemon=True).start()

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    with open('settings.yaml', 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
    config = result
    qq = int(config.get('机器人QQ'))
    key = config.get("ws-key")
    port = int(config.get("ws-port"))
    bot = Mirai(qq, adapter=WebSocketAdapter(
        verify_key=key, host='localhost', port=port
    ))
    master = int(config.get('masterQQ'))

    # 芝士logger
    logger = newLogger()
    logger.info("欢迎使用")
    logger.info("项目所有权：https://github.com/avilliai")
    main(bot, logger)
    # 在主函数中开启UI线程
    run_ui_in_thread(bot, logger)

    try:
        bot.run()
    except Exception as e:
        logger.error(e)
        input("出错，按任意键退出")

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
