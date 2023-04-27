SUDO = list(set(int(x) for x in os.environ.get("SUDO", "5985715321").split()))

@app.on_message(f.command("ship") & f.user(SUDO))
async def couple(client, message: Message):
    if message.chat.type == "private":
        await message.reply_text("Grupta Çalıştır.")
        return
    try:
        m = await message.reply("Shipliyom...")
        await asyncio.sleep(1.0)
        humay = get_text(message)
        if not humay:
            humay = "Aşk ❤️:"
        mentions = ""
        list_of_users = []
        async for mentions in client.iter_chat_members(message.chat.id):  
            if not mentions.user.is_bot: 
                list_of_users.append(mentions.user.id)
        if len(list_of_users) < 2:
            await message.reply_text("Yeterli birey yok.")
            return
        m1_id = random.choice(list_of_users)
        m2_id = random.choice(list_of_users)
        while m1_id == m2_id:
            m1_id = random.choice(list_of_users)
        m1_mention = (await client.get_users(m1_id)).mention
        m2_mention = (await client.get_users(m2_id)).mention
        h = f"{humay}\n\n{m1_mention} + {m2_mention} = ❤️"
        await client.send_message(message.chat.id, h)
        await m.delete()
    except Exception as e:
        print(e)
        await message.reply_text(f"Hata: {e}\n\n@mmagneto'ya bildir!")
