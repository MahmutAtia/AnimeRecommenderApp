import React from "react";

export default function Card({
  title,
  synopsis,
  img_url,
  recommend_url,
  recommend,
  key,
  genre,
}) {
  const handle_click = function () {
    recommend(recommend_url);
  };

  return (
    <div>
      <div className=" hover:bg-gray-100 w-5/6 hover:w-11/12 h-[430px] hover:h-[440px] hover:drop-shadow-2xl max-w-sm rounded overflow-hidden shadow-lg cursor-pointer duration-1000">
        {/* overlayer with the image in one container */}
        <div onClick={handle_click} className="group relative w-full ">
          <div class="absolute top-0 left-0 w-full h-0 flex flex-col justify-center items-center bg-indigo-100 opacity-0 group-hover:h-full group-hover:opacity-90 duration-500">
            <h1 class="text-2xl text-black font-bold">Recomend Similar</h1>
          </div>
          <img
            className="w-full h-32 object-cover"
            src={img_url}
            alt="Sunset in the mountains"
          />
        </div>

        {/* overlayer with the text in one container */}
        
        <div className="group relative w-full h-full">
          <div class="absolute bottom-0 left-0 w-full h-0 flex flex-col justify-center items-center bg-red-100 opacity-0 group-hover:h-full group-hover:opacity-90 duration-500">
            <h1 class="text-2xl text-black font-bold">See Details</h1>
          </div>
          <div className="px-6 py-4">
            <div className="font-bold text-xl mb-2">{title}</div>
            <p className="text-gray-700 text-base">
              {synopsis.substring(0, 100) + "..."}
            </p>
          </div>

          <div className="px-6 pt-1 pb-2">
            
            {genre.map((obj,key)=>(
                <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
              {obj.name}
            </span>
            ))}
            
           
          </div>
        </div>
        
      </div>
    </div>
  );
}
