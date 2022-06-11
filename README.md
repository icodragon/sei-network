# sei-network
Useful scripts

<b>autodelegate.py</b> - Script autodelegate and claim rewards.

<h2>Install</h2>
<code>apt install python3-pip</code></br>
<code>wget https://raw.githubusercontent.com/icodragon/sei-network/main/autodelegate.py</code></br>
<code>wget https://raw.githubusercontent.com/icodragon/sei-network/9d637172046af57b02f2e2cf28b9056e2302c644/requirements.txt</code></br>
<code>pip3 install -r requirements.txt</code></br>
Start scripts</br>
<code>python3 autodelegate.py VALOPER_ADDRESS WALLET_ADDRESS PASSWORD_WALLET_ADDRESS></code></br>

For start in handless mode.</br>
<code>apt install screen</code></br>
<code>screen -S autodelegate</code></br>
<code>python3 autodelegate.py VALOPER_ADDRESS WALLET_ADDRESS PASSWORD_WALLET_ADDRESS></code></br>
Exit in screen (CRTL + A + D)</br>
Connect in screen (screen -X autodelegate)</br>
