# **KeyZero: Bitcoin Private Key Brute Force Tool** [![CodeFactor](https://www.codefactor.io/repository/github/vlnahp/KeyZero/badge/main)](https://www.codefactor.io/repository/github/vlnahp/KeyZero/overview/main)

KeyZero is a Python-based tool designed for brute-forcing Bitcoin private keys. It generates random or sequential private keys, computes their corresponding public addresses, and checks them against an online API or an offline database to determine if they hold any Bitcoin balance. The name "KeyZero" humorously reflects the near-zero chance of finding a valid key, making it a fun and educational tool for exploring Bitcoin's security.

---

## **Features**
- **Efficiency**: Utilizes the `bit` library for fast key generation and address computation.
- **Flexibility**: Supports both online and offline modes for address checking.
- **User Interaction**: Provides an interactive command-line interface for ease of use.
- **Results Storage**: Saves found keys to `foundkey.txt`.
- **Progress Tracking**: Displays the number of keys checked per second and elapsed time.
- **Resume Functionality**: Can resume sequential brute-forcing from where it left off using a cache file (`cache.txt`).

---

## **Quick Start**

1. **Clone the Repository**:
   ```bash
   $ git clone https://github.com/vlnahp/KeyZero.git
   ```

2. **Navigate to the Directory**:
   ```bash
   $ cd KeyZero
   ```

3. **Install Dependencies**:
   ```bash
   $ pip install -r requirements.txt
   ```

4. **Run the Tool**:
   ```bash
   $ python KeyZero.py  # or python3 KeyZero.py on Linux
   ```

---

## **Requirements**

- **Offline Mode**: Requires a database of Bitcoin addresses. By default, `address.txt` is used, which contains a limited set of addresses. For a comprehensive database, download the latest address list from [here](http://addresses.loyce.club/) and replace `address.txt`. Ensure your system has sufficient RAM to handle large databases.

---

## **Usage**

Execute the tool and follow the on-screen instructions to select your desired action. The tool will guide you through the process of generating and checking private keys.

### **Options**
1. **Generate Random Key Pair**: Creates a random Bitcoin private key and public address.
2. **Generate Address from Private Key**: Computes the public address for a given private key.
3. **Brute-Force Bitcoin (Offline Mode)**: Checks generated addresses against a local database.
4. **Brute-Force Bitcoin (Online Mode)**: Checks generated addresses against the Blockchain API.

---

## **License**

KeyZero is licensed under a strong copyleft license, ensuring that any modifications or larger works using this tool must also be open-sourced under the same license. This includes preserving copyright and license notices and providing an express grant of patent rights. If a modified version is used to provide a service over a network, the complete source code of the modified version must be made available.

---

## **Latest Release**

Download the latest version (v1.2.0) from [here](https://github.com/vlnahp/KeyZero/releases/download/v1.2.1/KeyZero-windows64-v.1.2.0.tar.xz).

---

## **Disclaimer**

The primary goal of KeyZero is educational, aimed at learning Python and understanding Bitcoin's security mechanisms. It is not intended for malicious purposes. The security of Bitcoin remains robust, especially against classical computing threats. However, the advent of quantum computing could pose future challenges.

---

## **Contributing**

Contributions are welcome! Please ensure that any modifications adhere to the licensing terms and include appropriate documentation. To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

---

## **Support**

For issues or support, please open an issue on the [GitHub repository](https://github.com/vlnahp/KeyZero/issues).

---

## **Why "KeyZero"?**

The name "KeyZero" humorously reflects the near-zero chance of finding a valid Bitcoin private key through brute-forcing. It serves as a reminder of the immense security of Bitcoin's cryptographic design while providing a fun and educational tool for exploring its mechanics.

---

## **Tagline**

*"Chasing the impossible, one key at a time."*

---

This documentation provides a comprehensive guide to KeyZero. If you have any questions or need further assistance, feel free to reach out!
