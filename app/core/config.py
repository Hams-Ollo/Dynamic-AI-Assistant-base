"""
Configuration management for the application.
"""
import os
from pathlib import Path
from typing import Dict, Any, Optional

import streamlit as st
from dotenv import load_dotenv

def get_env_or_secret(key: str, default: Any = None) -> Any:
    """Get value from environment or Streamlit secrets."""
    # Try Streamlit secrets first
    try:
        return st.secrets[key]
    except (KeyError, AttributeError):
        # Fallback to environment variable
        return os.getenv(key, default)

def load_config(config_path: Optional[str] = None) -> Dict[str, Any]:
    """Load application configuration from environment and config files."""
    # Load environment variables
    env_path = Path('.env')
    load_dotenv(env_path if env_path.exists() else '.env.example')
    
    # Debug print (masked for security)
    api_key = get_env_or_secret('GROQ_API_KEY', '')
    print(f"Debug - GROQ_API_KEY loaded: {'*' * 4}{api_key[-4:] if api_key else 'Not found'}")
    
    config = {
        # Core settings
        'env': get_env_or_secret('APP_ENV', 'development'),
        'debug': get_env_or_secret('DEBUG', 'false').lower() == 'true',
        'log_level': get_env_or_secret('LOG_LEVEL', 'INFO'),
        
        # API settings
        'api': {
            'host': get_env_or_secret('API_HOST', 'localhost'),
            'port': int(get_env_or_secret('API_PORT', '8000')),
        },
        
        # Agent settings
        'agent': {
            'api_key': api_key,
            'model': get_env_or_secret('MODEL_NAME', 'mixtral-8x7b-32768'),
            'temperature': float(get_env_or_secret('MODEL_TEMPERATURE', '0.7')),
        },
        
        # Memory settings
        'memory': {
            'type': get_env_or_secret('MEMORY_TYPE', 'vector'),
            'backend': get_env_or_secret('MEMORY_BACKEND', 'chroma'),
            'path': get_env_or_secret('MEMORY_PATH', './data/memory'),
        }
    }
    
    return config
