

# Btcbf: Bitcoin Private Key Brute Force Tool [![CodeFactor](https://www.codefactor.io/repository/github/vlnahp/btcbf/badge/main)](https://www.codefactor.io/repository/github/vlnahp/btcbf/overview/main)

Btcbf is a Python-based tool developed for brute-forcing Bitcoin private keys. It generates random or sequential private keys, computes their corresponding public addresses, and checks them against an online API or an offline database to determine if they hold any Bitcoin balance.

## Features
- **Efficiency**: Utilizes the `bit` library for fast key generation and address computation.
- **Flexibility**: Supports both online and offline modes for address checking.
- **User Interaction**: Provides an interactive command-line interface for ease of use.
- **Results Storage**: Saves found keys to `foundkey.txt`.

## Quick Start

1. **Clone the Repository**:
   ```bash
   $ git clone https://github.com/vlnahp/Btcbf.git
   ```

2. **Navigate to the Directory**:
   ```bash
   $ cd Btcbf
   ```

3. **Install Dependencies**:
   ```bash
   $ pip install -r requirements.txt
   ```

4. **Run the Tool**:
   ```bash
   $ python Btcbf.py  # or python3 Btcbf.py on Linux
   ```

## Requirements

- **Offline Mode**: Requires a database of Bitcoin addresses. By default, `address.txt` is used, which contains a limited set of addresses. For a comprehensive database, download the latest address list from [here](http://addresses.loyce.club/) and replace `address.txt`. Ensure your system has sufficient RAM to handle large databases.

## Usage

Execute the tool and follow the on-screen instructions to select your desired action. The tool will guide you through the process of generating and checking private keys.

## License

Btcbf is licensed under a strong copyleft license, ensuring that any modifications or larger works using this tool must also be open-sourced under the same license. This includes preserving copyright and license notices and providing an express grant of patent rights. If a modified version is used to provide a service over a network, the complete source code of the modified version must be made available.

## Latest Release

Download the latest version (v1.2.0) from [here](https://github.com/vlnahp/Btcbf/releases/download/v1.2.1/Btcbf-windows64-v.1.2.0.tar.xz).

## Disclaimer

The primary goal of Btcbf is educational, aimed at learning Python and understanding Bitcoin's security mechanisms. It is not intended for malicious purposes. The security of Bitcoin remains robust, especially against classical computing threats. However, the advent of quantum computing could pose future challenges.

## Contributing

Contributions are welcome! Please ensure that any modifications adhere to the licensing terms and include appropriate documentation.

## Support

For issues or support, please open an issue on the [GitHub repository](https://github.com/vlnahp/Btcbf/issues).
