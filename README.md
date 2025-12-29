# n8n_workflow
This repo includes details related to a simple n8n workflow creation. This workflow/AI app was built mainly to red team this worklfow against open source versions giskard, garak, prompfoo adn deepeval to study various capabilities present in these tools.


Note:- I am using free, open-source version of n8n for this exploration. See license and NOTICE.md for details about re-use.

## Start n8n
```
n8n start
```

## Installation
I am following the node approach. Please feel free to use the docker approach if you would like.

OS:- Ubuntu 24.04.3 LTS

```
sudo apt update
```
Install nvm
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

Reload bashrc/zshrc 
```
source ~/.bashrc
```
Check nvm installation
```
nvm --version
```

Install node.js - 🚨 Note that n8n requires versions between 20.19 and 24.x, inclusive - as of December 16, 2025
```
nvm install 20
nvm use 20
nvm alias default 20
```

Verify
```
node -v
#Should say whatever version you installed
```

Install / Run n8n
```
npx n8n
```
If the above doesn't work try
```
npm install n8n -g
```
Open http://localhost:5678 in your browser



## License

- Workflow definitions in this repository are licensed under the MIT License.
- n8n itself is licensed separately. Please check out their repo here <a>https://github.com/n8n-io/n8n?tab=License-1-ov-file </a> for further info.
