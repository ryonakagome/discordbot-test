import discord

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました。')


@client.event
async def on_message(message):
    if message.content.startswith('./neko'):
        reply = 'にゃーん'
        await client.send_message(message.channel, reply)

client.run('NTI3OTE2Nzc1MjI1MTYzNzc5.D3-VoA.yQYq5w1qblUam9q6VicdTaaeEXE')