
// import Card from '../components/card';
import { useState,useEffect,useContext } from 'react';
import axios from "axios";
import Sidebar from '../components/sidebar';
import Overlay from '../components/overlay';
import { PaginationNav1Presentation } from '../components/pagation';
import Search from '../components/Search';
import {kebabCase} from "kebab-case"
import React from 'react';
import store from '../store'
import { Provider } from 'react-redux';
import { redirect,useNavigate} from 'react-router-dom';
import { UserContext } from '../UserContext';
const LazyCard = React.lazy(()=>import("../components/card"))





function List_page() {
const [data,setData] = useState()
// const [q, setq] = useState("");
const [url,setUrl] = useState("http://127.0.0.1:8000/animes/")
const [genre,setGenre] = useState()
const [header,setHeader] = useState("All Animes")
const navigate = useNavigate();
const setToken= useContext(UserContext).setToken;

console.log( useContext(UserContext).user);

const recomend = function(url){
  
  setUrl(url)
}

const pull_title = function(header){
    setHeader("MOST SIMILAR ANIMES TO: " + header.toUpperCase())
    
}

const pull_q = function(data){
    data = data.replace(" ","-")
    if(data)    
    {setUrl("http://localhost:8000/animes/search/"+data)}
}

useEffect(() => {
  const token = localStorage.getItem("token")
  console.log(token)
  setToken(token)
  axios.get(url).then((res)=>{
    setData(res.data)

    axios.get("http://127.0.0.1:8000/animes/genre/", ).then((res)=>{
        setGenre(res.data.results)
      })
  })
 
}, [url]);

if (!data) return []; // very important
if(!genre) return []
// console.log(data.results[0].genre)







  return (
    <div>
           
     <button onClick={()=>navigate("/login")}> redirect</button>

    <Search
    func = {pull_q}
     />
    <div className=' flex flex-row p-10'>

    {/* <div className=" top-0 ">
      <Sidebar genre = {genre} />
      </div> */}

    {/* column for header and cards */}
    <div className='flex flex-col'>
    <h1 className='text-4xl font-bold m-16 leading-relaxed border-b font-serif ml-10'>{header}</h1>
      
    <div className="flex-[0.9] grid gap-6 lg:grid-cols-4 p-5 ">
    <React.Suspense fallback="Louding ..">
     
{
  data.results.map((obj,key)=>(
    
      <LazyCard 
     key={obj.id}
     title = {obj.title}
     synopsis = {obj.synopsis}
     img_url = {obj.img_url}
     recommend = {recomend}
     recommend_url = {obj.recommend_url}
     genre= {genre.filter((x,i)=>obj.genre.includes(i))}
     func = {pull_title}
     id = {obj.id}
     obj = {obj}
     />

    ))}
     </React.Suspense>

    </div>
    </div>
    {/* <PaginationNav1Presentation
    count={ data.count}
    index = {data.results.length}

     /> */}
    </div>
    </div>
      
  );
}

export default List_page;
