
import axios from 'axios';
import React, {useState} from 'react'
import { useSignIn } from 'react-auth-kit';




export default function Login() {
    const [user, setuser] = useState("username");
const [pass, setpass] = useState("pass");
const signin = useSignIn()

const url = "http://localhost:8000/login/"
const handleSubmit =  (e)=>{
    e.preventDefault();
    
         axios.post(url,{username:user,password:pass}).then(res=>{
            console.log(res.data)
            signin({
                token: res.data.token,
                expiresIn:36000,
                tokenType: "Token",
               })
            
         }).catch(err=>{console.log(err)}) 

        
        }
      

  return (
    <div>
    <form>
        <input value={user} onChange={(e)=>setuser(e.target.value)} placeholder='username' />
        <input value={pass} onChange={(e)=>setpass(e.target.value)} placeholder='Password'/>
        <input onClick={handleSubmit} value="submit" type="submit"/>
    </form>
  </div>
  )
}
