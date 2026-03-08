users = {}

def main():
    while True:
        print("\n" + "="*30)
        choice = input("請選擇操作選項 (輸入 a 註冊, 輸入 b 登入, 輸入 c 退出 )？ ").strip().lower()

        if choice == 'a':
            while True:
                username = input("請輸入帳號：").strip()
                if not username:
                    print("帳號不能為空，請重新輸入！")
                    continue
                
                if username in users:
                    print("帳號已存在，請重新輸入！")
                else:
                    password = input("請輸入密碼：").strip()
                    if not password:
                        print("密碼不能為空，請重新輸入！")
                        continue
                    
                    users[username] = password
                    print("註冊成功！")
                    break 

        elif choice == 'b':
            username = input("請輸入帳號：").strip()
            password = input("請輸入密碼：").strip()
            
            if users.get(username) == password:
                print(f"歡迎回來，{username}！登入成功。")
            else:
                print("帳號或密碼錯誤！")

        elif choice == 'c':
            print("程式已退出，再見！")
            break

        else:
            print("無效的選項，請輸入 a, b 或 c！")

if __name__ == "__main__":
    main()
