import axios from "axios";
import React, { useState,useContext } from "react";
import { useSignIn } from "react-auth-kit";
import { redirect,useNavigate } from "react-router-dom";
import { UserContext } from "../UserContext";

export default function Login() {
  const navigate = useNavigate();

  const [user, setuser] = useState("username");
  const [pass, setpass] = useState("pass");
  const signin = useSignIn();
  const {value,setValue} = useContext(UserContext)
  console.log(value)

  const url = "http://localhost:8000/login/";
  const handleSubmit = (e) => {
    e.preventDefault();

    axios
      .post(url, { username: user, password: pass })
      .then((res) => {
        console.log(res.data);
        setValue(res.data.token)
       
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <div>
      <form>
        <input
          value={user}
          onChange={(e) => setuser(e.target.value)}
          placeholder="username"
        />
        <input
          value={pass}
          onChange={(e) => setpass(e.target.value)}
          placeholder="Password"
        />
        <input onClick={handleSubmit} value="submit" type="submit" />
        <button onClick={() => redirect("/")}> redirect</button>
      </form>
    </div>
  );
}
