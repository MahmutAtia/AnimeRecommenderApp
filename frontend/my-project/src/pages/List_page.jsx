
import Card from '../components/card';
import { useState,useEffect } from 'react';
import axios from "axios";
import Sidebar from '../components/sidebar';
import Overlay from '../components/overlay';
import { PaginationNav1Presentation } from '../components/pagation';
import Search from '../components/Search';
import {kebabCase} from "kebab-case"



function List_page() {
const [data,setData] = useState()
// const [q, setq] = useState("");
const [url,setUrl] = useState("http://127.0.0.1:8000/animes/")
const [genre,setGenre] = useState()



const recomend = function(url){
  setUrl(url)
}
const pull_q = function(data){
    data = data.replace(" ","-")
    if(data)    
    {setUrl("http://localhost:8000/animes/search/"+data)}
}


useEffect(() => {
  axios.get(url).then((res)=>{
    setData(res.data)

    axios.get("http://127.0.0.1:8000/animes/genre/").then((res)=>{
        setGenre(res.data.results)
      })
  })
 
}, [url]);

if (!data) return []; // very important
if(!genre) return []
// console.log(data.results[0].genre)




  return (
    <div>
    <Search
    func = {pull_q}
     />
    <div className=' flex flex-row p-2'>

    <div className=" top-0 ">
      <Sidebar genre = {genre} />
      </div>
    <div className="flex-[0.9] grid gap-6 lg:grid-cols-3 ">
    
    
{
  data.results.map((obj,key)=>(
      <Card 
     key={obj.id}
     title = {obj.title}
     synopsis = {obj.synopsis}
     img_url = {obj.img_url}
     recommend = {recomend}
     recommend_url = {obj.recommend_url}
     genre= {genre.filter((x,i)=>obj.genre.includes(i))}
     />

    ))}
     

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
