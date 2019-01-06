import term, appglue, sys, badge

term.empty_lines()
nickname = badge.nvs_get_str("owner", "name", "")
nickname = term.prompt("Configure nickname", 1, 3, nickname)
badge.nvs_set_str("owner", "name", nickname)
appglue.home()
