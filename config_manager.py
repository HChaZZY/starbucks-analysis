"""
Configuration Manager Module

This module provides a ConfigManager class for managing configuration settings for the Starbucks Global Store Data Analysis Program.

The ConfigManager class handles reading from and writing to a JSON configuration file, allowing easy access and modification of program settings.

Classes:
    ConfigManager: Manages configuration settings stored in a JSON file.

Dependencies:
    json: For reading and writing JSON files.
    typing: For type hinting.
"""

import json
from typing import Dict, Any

class ConfigManager:
    """
    A class for managing configuration settings.

    This class provides methods to read from and write to a JSON configuration file,
    as well as to get and set individual configuration values.

    Attributes:
        config (Dict[str, Any]): A dictionary containing the configuration settings.

    Methods:
        __init__(self, config_file: str = 'config.json'): Initialize the ConfigManager with a specified config file.
        get(self, key: str) -> Any: Retrieve a configuration value by its key.
        set(self, key: str, value: Any) -> None: Set a configuration value for a given key.
        save(self, config_file: str = 'config.json') -> None: Save the current configuration to a JSON file.
    """

    def __init__(self, config_file: str = 'config.json'):
        """
        Initialize the ConfigManager with a specified config file.

        Args:
            config_file (str): The path to the JSON configuration file. Defaults to 'config.json'.
        """
        with open(config_file, 'r') as f:
            self.config: Dict[str, Any] = json.load(f)

    def get(self, key: str) -> Any:
        """
        Retrieve a configuration value by its key.

        Args:
            key (str): The key of the configuration setting to retrieve.

        Returns:
            Any: The value associated with the given key, or None if the key doesn't exist.
        """
        return self.config.get(key)

    def set(self, key: str, value: Any) -> None:
        """
        Set a configuration value for a given key.

        Args:
            key (str): The key of the configuration setting to set.
            value (Any): The value to associate with the given key.
        """
        self.config[key] = value

    def save(self, config_file: str = 'config.json') -> None:
        """
        Save the current configuration to a JSON file.

        Args:
            config_file (str): The path where the configuration file should be saved. Defaults to 'config.json'.
        """
        with open(config_file, 'w') as f:
            json.dump(self.config, f, indent=4)
