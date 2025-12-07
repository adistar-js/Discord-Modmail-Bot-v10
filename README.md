# 🎫 Discord Ticket Bot — Setup & Usage Guide

## 📌 **Setup Instructions**

Follow the steps below to configure your bot properly:

### 1️⃣ **Open the `config.json` file**

Fill in the required fields as shown:

1. **Bot Token (Line 2)**

   ```json
   "TOKEN": "your_bot_token_here",
   ```

2. **Bot Prefix (Line 4)**
   Set any prefix you want (example: `?`, `!`, `.`)

   ```json
   "PREFIX": "?",
   ```

3. **Staff / Support Role (Line 6)**
   Use the role mention format:

   ```json
   "STAFF_ROLE": "<@&role_id_here>",
   ```

4. **Private Category Name (Line 8)**
   This must match EXACTLY the category name in your server:

   ```json
   "PRIVATE_CATEGORY_NAME": "help-tickets",
   ```

> 💡 **Tip:** The safest option is to copy & paste the exact category name from Discord.

---

### 2️⃣ **Run the Program**

Start the bot normally.
If this is your first time running it, the setup may take a few minutes while dependencies are installed.

---

## ⚠️ **Important Notices**

* Ensure the **ticket category is private**, so only staff can view created tickets.
* The **category name must match exactly** with what you put in the config file.
* The bot **must have permissions** to create and delete channels.
* If you need help naming the bot or configuring the server, feel free to DM the developer.

---

# 🎟️ Creating a Ticket

Here is how users can create support tickets:

1. **DM the bot.**
   The bot will automatically generate a new private channel with the name:

   ```
   user.id
   ```

2. **Start chatting** inside the created ticket channel.

3. **Attachments**
   (Currently **not supported** — coming in a future update.)

4. **Closing a Ticket**
   Use the prefix + `close` command, for example:

   ```
   ?close
   ```

---

## ❤️ Thank You!

Thank you for using this Ticket Bot.
If you need help, feel free to reach out!
