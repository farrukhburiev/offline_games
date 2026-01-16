"""
Telegram Bot for Offline Games Mini App
Uses aiogram library to manage bot commands and inline keyboards
"""

import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.fsm.context import FSMContext

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ============================================================================
# Configuration
# ============================================================================

BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN not found! Set it in Railway.")

# Your game URLs (you can keep these or also make them env variables)
GAME_URL = "https://farrukhburiev.github.io/offline_games/"
MINESWEEPER_URL = "https://farrukhburiev.github.io/offline_games/?game=minesweeper"

# Initialize bot
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Replace with your GitHub Pages link (or any hosting URL for the Mini App)
# This URL should point to where you've deployed the index.html file
BASE_URL = "https://farrukhburiev.github.io/offline_games/"

# ============================================================================
# Initialize Bot and Dispatcher
# ============================================================================

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ============================================================================
# Keyboard Builders
# ============================================================================

def get_game_keyboard() -> InlineKeyboardMarkup:
    """
    Creates an inline keyboard with game launch buttons.
    
    WebAppInfo opens a Mini App within Telegram that loads the specified URL.
    URL Parameters:
    - BASE_URL: Opens the main game menu
    - BASE_URL?game=minesweeper: Automatically launches the Minesweeper game
    
    Returns:
        InlineKeyboardMarkup: Inline keyboard with game buttons
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎮 Open Game Center",
                    web_app=WebAppInfo(url=BASE_URL)
                )
            ],
            [
                InlineKeyboardButton(
                    text="💣 Play Minesweeper",
                    web_app=WebAppInfo(url=f"{BASE_URL}?game=minesweeper")
                )
            ]
        ]
    )
    return keyboard

# ============================================================================
# Command Handlers
# ============================================================================

@dp.message(CommandStart())
async def start_handler(message: types.Message, state: FSMContext) -> None:
    """
    Handles the /start command.
    
    When a user starts the bot, they receive a welcome message with
    an inline keyboard to launch the game or open the game center.
    
    Args:
        message: The Telegram message object
        state: FSM context for managing conversation state
    """
    welcome_text = (
        "👾 <b>Welcome to Offline Games!</b>\n\n"
        "🎮 Enjoy our collection of games right inside Telegram.\n\n"
        "Click a button below to get started:"
    )
    
    await message.answer(
        text=welcome_text,
        reply_markup=get_game_keyboard(),
        parse_mode="HTML"
    )
    logger.info(f"User {message.from_user.id} started the bot")


@dp.message(Command("game"))
async def game_handler(message: types.Message, state: FSMContext) -> None:
    """
    Handles the /game command.
    
    Sends the game launcher keyboard allowing users to choose which game to play.
    This is useful as an alternative way to access games.
    
    Args:
        message: The Telegram message object
        state: FSM context for managing conversation state
    """
    game_text = (
        "🎮 <b>Choose Your Game</b>\n\n"
        "Select a game to launch:"
    )
    
    await message.answer(
        text=game_text,
        reply_markup=get_game_keyboard(),
        parse_mode="HTML"
    )
    logger.info(f"User {message.from_user.id} requested /game command")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Fallback handler for unrecognized commands.
    
    Provides helpful information about available commands.
    
    Args:
        message: The Telegram message object
    """
    help_text = (
        "❓ <b>Unknown Command</b>\n\n"
        "Available commands:\n"
        "• /start - Launch the bot and view games\n"
        "• /game - View available games\n"
        "• /help - Show this message\n\n"
        "Tap the buttons to open games in Telegram!"
    )
    
    await message.answer(
        text=help_text,
        parse_mode="HTML"
    )

# ============================================================================
# Main Entry Point
# ============================================================================

async def main() -> None:
    """
    Main entry point for the bot.
    
    Initializes the dispatcher and starts polling for updates from Telegram.
    This will run indefinitely until interrupted (Ctrl+C).
    """
    logger.info("🤖 Bot is starting...")
    logger.info(f"📱 Game Center URL: {BASE_URL}")
    logger.info(f"⛏️  Minesweeper URL: {BASE_URL}?game=minesweeper")
    
    try:
        # Start polling for updates
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as e:
        logger.error(f"❌ Error occurred: {e}")
    finally:
        # Clean up
        await bot.session.close()
        logger.info("🛑 Bot stopped")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot interrupted by user")
