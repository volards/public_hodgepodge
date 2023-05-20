def quick_job():
    with open("wallets_and_ammounts.txt", "r") as f:
        wallets_and_ammounts_list = [l.strip() for l in f]
    wallets = [l.split(" ")[0] for l in wallets_and_ammounts_list]
    wallets_sorted_by_frequency = sorted(wallets, key=lambda l: wallets.count(l), reverse=True)
    cheched_wallets = []
    final_dict = {}
    add_to_the_end = []
    for wallet in wallets_sorted_by_frequency:
        if wallet not in cheched_wallets:
            if wallets.count(wallet) > 8:
                this_wallet_ammounts_list = [l for l in wallets_and_ammounts_list if wallet == l.split(" ")[0]]
                first_part, second_part = this_wallet_ammounts_list[:8], this_wallet_ammounts_list[8:]
                # print(first_part, second_part)
                for k in range(0, 8):
                    final_dict[k*43 + len(cheched_wallets)] = first_part[k]
                add_to_the_end.extend(second_part)
            else:
                this_wallet_ammounts_list = [l for l in wallets_and_ammounts_list if wallet == l.split(" ")[0]]
                # print(this_wallet_ammounts_list)
                for k in range(0, wallets.count(wallet)):
                    place_to_put = 0
                    while (place_to_put + (k*43 + len(cheched_wallets))) in final_dict:
                        place_to_put +=1
                    final_dict[place_to_put + k*43 + len(cheched_wallets)] = this_wallet_ammounts_list[k]
            cheched_wallets.append(wallet)
    final_list = [v for k, v in sorted(final_dict.items())]
    final_list.extend(add_to_the_end)
    for i, l in enumerate(final_list):
        print(i, l)
