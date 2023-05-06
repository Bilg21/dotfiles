require("bilg.base") 			-- General Settings
require("bilg.plugins") 		-- Plugins
require("bilg.highlights")	 	-- Colourscheme and other highlights
require("bilg.remaps") 			-- Keymaps
require("bilg.bootstrap") 		-- Packer Auto-Installer

---Pretty print lua table
function _G.dump(...)
	local objects = vim.tbl_map(vim.inspect, { ...})
	print(unpack(objects))
end
	
