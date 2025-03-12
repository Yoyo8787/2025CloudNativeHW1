import re
from factories.service_factory import ServiceFactory

def parse_command(user_input):
    # 這是用來處理帶有單引號的參數（例如：'Phone model 8'）
    pattern = r"([^\s']+|'[^']*')"
    return [arg.strip("'") for arg in re.findall(pattern, user_input)]

def main():
    service_factory = ServiceFactory()
    user_controller = service_factory.get_user_controller()
    listing_controller = service_factory.get_listing_controller()
    category_controller = service_factory.get_category_controller()

    # 用戶互動邏輯或 API 請求邏輯
    while True:
        try:
            user_input = input("# ").strip()
            if not user_input:
                continue

            args = parse_command(user_input)  # 使用正則處理命令和參數
            command = args[0].upper()

            if command == "REGISTER" and len(args) == 2:
                print(user_controller.register(args[1]))

            elif command == "CREATE_LISTING" and len(args) == 6:
                # 請注意參數的處理
                print(listing_controller.create_listing(args[1], args[2], args[3], int(args[4]), args[5]))

            elif command == "GET_LISTING" and len(args) == 3:
                print(listing_controller.get_listing(args[1], int(args[2])))

            elif command == "DELETE_LISTING" and len(args) == 3:
                print(listing_controller.delete_listing(args[1], int(args[2])))

            elif command == "GET_CATEGORY" and len(args) == 3:
                print(category_controller.get_category(args[1], args[2]))

            elif command == "GET_TOP_CATEGORY" and len(args) == 2:
                print(category_controller.get_top_category(args[1]))

            elif command == "USER" and len(args) == 1:
                print(user_controller.list_users())

            else:
                print("Error - invalid command format")

        except Exception as e:
            print(f"Error - {str(e)}")

if __name__ == "__main__":
    main()