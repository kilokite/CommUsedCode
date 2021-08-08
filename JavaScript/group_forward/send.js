const oicq = require("oicq"); //OICQ bot模块
const chalk = require('chalk')

const client = oicq.createClient(账号)//c
//直接往上加
const group = {
    909932160:false, //false和true都⭐
    939869720:true,
    453864175:true,
}
//监听上线事件
client.on("system.online", () => 
    console.log(chalk.yellow('登录成功2323'))
);

client.on("message.group", (data)=>{
    var group_id = data.group_id
    console.log(group_id)
    if(typeof(group[group_id]) != 'undefined'){
        for(id in group){
            if(id != group_id ){
           // console.log(id)
            var req_msg = `\
${data.raw_message}\n
来自群：${data.group_name}
发送者：${data.sender.nickname}
群ID：${data.group_id}
发送者ID：${data.sender.user_id}`
            client.sendGroupMsg(id, req_msg)
            }
        }
    }
})

client.login("密码");
