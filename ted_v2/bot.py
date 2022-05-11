import json
import lightbulb

with open("ted_v2/settings.json", 'r') as settings_file:
    settings = json.load(settings_file)

bot = lightbulb.BotApp(token=settings["token"], prefix="$")


@bot.command
@lightbulb.command("test", "test")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond("you passed")


bot.run()
