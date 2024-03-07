from VKDT.Discord.discord_commands.CommandSettings import client
print('ALLO')

@client.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(client))