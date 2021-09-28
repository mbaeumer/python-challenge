

def solve():
    simple_pirates = 1
    coins = 119
    found = False

    while simple_pirates < 100:
        simple_reward = 0
        while simple_reward < 100:
            simple_reward = simple_reward + 1
            deputy_reward = 2 * simple_reward
            chief_reward = 5 * simple_reward
            result = simple_pirates * simple_reward + deputy_reward + chief_reward
            print("Result: pirates=%d, reward=%d, result=%d" % (simple_pirates, simple_reward, result))
            if result > coins:
                break
            elif result == coins:
                found = True
                break
        if found:
            break
        simple_pirates = simple_pirates + 1

if __name__ == '__main__':
    solve()