import json

from beans_manager.badge_manager import BadgeManager

def main():

    for element in BadgeManager().select_all_active_badges():
        print( f'@Debug: element = { json.dumps(element.__dict__) }\n' )

if __name__ == '__main__':
    main()