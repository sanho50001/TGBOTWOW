from VKDT.Discord.discord_commands.CommandSettings import client


@client.command()
async def exit(ctx):
    owner = ctx.message.author

    await ctx.send('Все куда, а я ухожу')
    print(f'{client.user.name}: Бот отключается')
    if owner:
        await ctx.send('Хозяин приказал отключиться')
        print(f'{client.user.name}: Экстренное закрытие')
        exit()
