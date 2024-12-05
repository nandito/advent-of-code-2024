import logging
import re

def solve_part1(lines):
    ordering_rule_re = r"(\d+)\|(\d+)"
    ordering_rules = []
    pages_to_produce = []

    for line in lines:
        line = line.strip()
        if line == "":
            continue
        if re.match(ordering_rule_re, line):
            rule = [int(p) for p in line.split("|")]
            ordering_rules.append(rule)
        else:
            page_to_produce = [int(p) for p in line.split(",")]
            pages_to_produce.append(page_to_produce)

    logging.debug("Ordering rules: " + str(ordering_rules))
    logging.debug("Pages to produce: " + str(pages_to_produce))

    valid_orders = []
    for produce_list in pages_to_produce:
        logging.debug("Page to produce: " + str(produce_list))

        valid_order = True
        order = []
        for page in produce_list:
            order.append(page)
            related_orders = [o[1] for o in ordering_rules if o[0] == page]
            logging.debug("Related orders: " + str(related_orders))

            for related_order in related_orders:
                if related_order in order:
                    valid_order = False
                    break

        if valid_order:
            valid_orders.append(order)

    logging.debug("Valid orders: " + str(valid_orders))

    middle_numbers = [n[len(n) // 2] for n in valid_orders]
    logging.debug("Middle numbers: " + str(middle_numbers))
    print("Sum of middle numbers: " + str(sum(middle_numbers)))


