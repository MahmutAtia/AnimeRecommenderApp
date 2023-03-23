import { useParams } from 'react-router-dom'

import React from 'react'

export default function Detail_page() {
  const {id}  =  useParams()
  console.log(id)
  return (
    <div>detail_page</div>
  )
}
