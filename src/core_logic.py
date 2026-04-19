from telegram.ext import ContextTypes
from telegram import ForceReply, Update
from soccer_http_client import FootballAPIClient



football_client = FootballAPIClient()


async def start_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    print(f"User {user} started the bot.")
    await update.message.reply_html(
        rf"Hola {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Hola, soy un bot de futbol desarrollado por Gabotdev. Puedo ayudarte a obtener informacion sobre equipos y jugadores")
    await update.message.reply_text("Para obtener informacion sobre un jugador, utiliza el comando /player seguido del apellido del jugador. Por ejemplo: /player Messi")
    await update.message.reply_text("Para obtener informacion sobre un equipo, utiliza el comando /team seguido del nombre del equipo o el pais que desees. Por ejemplo: /team FC Barcelona")

async def get_player(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /player is issued."""
    if context.args:
        player_name = " ".join(context.args)
        print(f"User requested information about player: {player_name}")
        # Aquí puedes agregar la lógica para obtener información sobre el jugador
        response = football_client.get_player_info(player_name)
        players = response['response']

        await update.message.reply_text(f"Encontré {len(players)} resultados para el jugador {player_name}.")

        for player_data in players:
            player = player_data['player']
            await update.message.reply_text(f"Nombre: {player['firstname']} {player['lastname']}\nEdad: {player['age']}\nPosición: {player['position']}")
            await update.message.reply_photo(photo=player['photo'])

    else:
        await update.message.reply_text("Por favor, proporciona el nombre del jugador después del comando. Por ejemplo: /player Lionel Messi")


async def get_team(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /team is issued."""
    if context.args:
        team_name = " ".join(context.args)
        print(f"User requested information about team: {team_name}")
        # Aquí puedes agregar la lógica para obtener información sobre el equipo


        response = football_client.get_team_info(team_name)
        teams = response['response']
        await update.message.reply_text(f"Encontré {len(teams)} resultados para el nombre {team_name}.")

        for team_data in teams:
            team = team_data['team']
            await update.message.reply_text(f"Nombre: {team['name']} \nFundado: {team['founded']}\nPaís: {team['country']}\nNacional: {'Sí' if team['national'] else 'No'}")
            await update.message.reply_photo(photo=team['logo'])
    else:
        await update.message.reply_text("Por favor, proporciona el nombre del equipo después del comando. Por ejemplo: /team FC Barcelona")