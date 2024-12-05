import logging
import re

def solve_part2(lines):
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

    invalid_orders = []
    for produce_list in pages_to_produce:

        order = []
        is_invalid_order = False
        for page in produce_list:
            if is_invalid_order:
                break
            order.append(page)
            related_orders = [o[1] for o in ordering_rules if o[0] == page]

            for related_order in related_orders:
                if related_order in order:
                    invalid_orders.append(produce_list)
                    is_invalid_order = True
                    break


    logging.debug("Invalid orders: " + str(invalid_orders))

    fixed_orders = []
    for invalid_order in invalid_orders:
        logging.debug("\n\nFixing invalid order: " + str(invalid_order))
        original_order = []
        for page in invalid_order:
            original_order.append(page)
            logging.debug("Page: " + str(page))
            related_orders = [o[1] for o in ordering_rules if o[0] == page]
            logging.debug("Related orders: " + str(related_orders))
            for related_order in related_orders:
                logging.debug("Related order: " + str(related_order))
                if related_order in original_order:
                    index = original_order.index(related_order)
                    logging.debug("Index of " + str(related_order) + " is " + str(index) + " so insert " + str(page) + " at " + str(index))
                    logging.debug("Original order before remove and insert: " + str(original_order))
                    original_order.remove(page)
                    original_order.insert(index, page)
                    logging.debug("Original order after remove and insert: " + str(original_order))

        logging.debug("Corrected order: " + str(original_order))
        fixed_orders.append(original_order)

    middle_numbers = [n[len(n) // 2] for n in fixed_orders]
    logging.debug("Middle numbers: " + str(middle_numbers))
    print("Sum of middle numbers: " + str(sum(middle_numbers)))
