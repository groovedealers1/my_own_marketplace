import axios from "axios";
import {useEffect, useState} from "react";

export default function Example() {

    const [wears, setWears] = useState([]);

    const getAllWears = () => {
        axios.get('http://localhost:8000/wears').then(r => {
            const allWears = r.data;
            const wearItems = allWears.map(w => {return {id: w.id, name: w.name, price: w.price, color: w.color, imageSrc: w.imageSrc, imageAlt: w.imageAlt};});
            setWears(wearItems);
        })
    }

    useEffect(() => {
        getAllWears()
    }, []);
    return (
        <div className="bg-white">
            <div className="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8">
                <center><h2 className="text-2xl font-bold tracking-tight text-gray-900">Stuff</h2></center>

                <div className="mt-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
                    {wears.map((w) => (
                        <div key={w.id} className="group relative">
                            <div className="aspect-h-1 aspect-w-1 w-full overflow-hidden rounded-md bg-gray-200 lg:aspect-none group-hover:opacity-75 lg:h-80">
                                <img
                                    alt={w.imageAlt}
                                    src={w.imageSrc}
                                    className="h-full w-full object-cover object-center lg:h-full lg:w-full"
                                />
                            </div>
                            <div className="mt-4 flex justify-between">
                                <div>
                                    <h3 className="text-sm text-gray-700">
                                        <a href={w.href}>
                                            <span aria-hidden="true" className="absolute inset-0" />
                                            {w.name}
                                        </a>
                                    </h3>
                                    <p className="mt-1 text-sm text-gray-500">{w.color}</p>
                                </div>
                                <p className="text-sm font-medium text-gray-900">{w.price}р</p>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}