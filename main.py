#!/usr/bin/env python3
"""
NGYT777GG WORM AI Telegram Bot with Flask Web Server

A professional Telegram bot with channel verification, Venice AI integration, 
admin broadcast functionality, and Flask web server for Render hosting.

Author: @GOAT_NG
"""

import logging
import asyncio
import threading
import os
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from bot_handlers import BotHandlers
from config import BOT_TOKEN
from app import app

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def start_flask_server():
    """Start Flask web server in a separate thread"""
    port = int(os.getenv('PORT', 5000))
    logger.info(f"馃寪 Starting Flask web server on port {port}...")
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)

def start_telegram_bot():
    """Start Telegram bot"""
    logger.info("馃殌 Starting NGYT777GG WORM AI Bot...")
    
    try:
        # Create the Application with better network settings for cloud deployment
        application = (Application.builder()
                      .token(BOT_TOKEN)
                      .connect_timeout(30)
                      .read_timeout(30)
                      .write_timeout(30)
                      .pool_timeout(1)
                      .build())
        
        # Initialize handlers
        handlers = BotHandlers()
        
        # Add command handlers
        application.add_handler(CommandHandler("start", handlers.start_command))
        application.add_handler(CommandHandler("menu", handlers.menu_command))
        application.add_handler(CommandHandler("clear", handlers.clear_command))
        application.add_handler(CommandHandler("broadcast", handlers.broadcast_command))
        application.add_handler(CommandHandler("help", handlers.help_command))
        
        # Add callback query handler for buttons
        application.add_handler(CallbackQueryHandler(handlers.button_callback))
        
        # Add message handler for regular messages
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.handle_message))
        
        logger.info("鉁� Bot handlers configured successfully")
        logger.info("馃攧 Starting bot polling...")
        
        # Start the bot with error resilience for cloud deployment
        application.run_polling(
            allowed_updates=["message", "callback_query"],
            poll_interval=1.0,
            timeout=20,
            bootstrap_retries=5,
            read_timeout=30,
            write_timeout=30,
            connect_timeout=30,
            pool_timeout=1
        )
        
    except Exception as e:
        logger.error(f"鉂� Critical error starting bot: {e}")
        logger.error(f"馃摑 Error details: {str(e)}")
        raise

def main():
    """Main function to start both Flask server and Telegram bot"""
    logger.info("馃殌 Starting NGYT777GG WORM AI Bot with Flask web server...")
    
    # Start Flask server in a separate thread
    flask_thread = threading.Thread(target=start_flask_server, daemon=True)
    flask_thread.start()
    logger.info("鉁� Flask web server started in background")
    
    # Start Telegram bot in main thread
    start_telegram_bot()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info("馃洃 Bot and web server stopped by user")
    except Exception as e:
        logger.error(f"鉂� Fatal error: {e}")
        raise
