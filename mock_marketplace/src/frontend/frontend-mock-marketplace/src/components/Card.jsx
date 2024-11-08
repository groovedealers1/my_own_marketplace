'use client'

import {useCallback, useEffect, useState} from 'react'
import { Radio, RadioGroup } from '@headlessui/react'
import axios from "axios";



const product = {
    name: 'Basic Tee 6-Pack',
    price: '$192',
    href: '#',
    images: [
        {
            src: 'https://tailwindui.com/plus/img/ecommerce-images/product-page-02-secondary-product-shot.jpg',
            alt: 'Two each of gray, white, and black shirts laying flat.',
        },
    ],
    colors: [
        { name: 'White', class: 'bg-white', selectedClass: 'ring-gray-400' },
        { name: 'Gray', class: 'bg-gray-200', selectedClass: 'ring-gray-400' },
        { name: 'Black', class: 'bg-gray-900', selectedClass: 'ring-gray-900' },
    ],
    sizes: [
        { name: 'S', inStock: true },
        { name: 'M', inStock: true },
        { name: 'L', inStock: true },
        { name: 'XL', inStock: true },
        { name: '2XL', inStock: true },
    ],
    description:
        'The Basic Tee 6-Pack allows you to fully express your vibrant personality with three grayscale options. Feeling adventurous? Put on a heather gray tee. Want to be a trendsetter? Try our exclusive colorway: "Black". Need to add an extra pop of color to your outfit? Our white tee has you covered.',

    details:
        'The 6-Pack includes two black, two white, and two heather gray Basic Tees. Sign up for our subscription service and be the first to get new, exciting colors, like our upcoming "Charcoal Gray" limited release.',
}

function classNames(...classes) {
    return classes.filter(Boolean).join(' ')
}


export default function Card () {
    const wearId = document.location.href.split('/')[4]

    const [selectedColor, setSelectedColor] = useState(product.colors[0])
    const [selectedSize, setSelectedSize] = useState(product.sizes[2])

    const [wear, setWears] = useState({images: {name_for_image_1: ''}});

    const getWear = () => {
        axios.get('http://127.0.0.1:8000/wears/' + wearId).then(r => {
            const stuff = r.data;
            console.log(stuff);
            setWears(stuff);
        })
    }

    useEffect(() => {
        getWear()
    }, []);


    return (
        <div className="bg-white">
            <div className="pt-6">

                {/* Image gallery */}
                <div className="mx-auto mt-6 max-w-2xl sm:px-6 lg:grid lg:max-w-7xl lg:grid-cols-3 lg:gap-x-8 lg:px-8">
                    <div className="aspect-h-4 aspect-w-3 hidden overflow-hidden rounded-lg lg:block">
                        {/*{wear.map((image) => (*/}
                        <img
                            alt='sorry we cant load the images'
                            // src={product.images[0].src}
                            src={'/images/' + wear.images.name_for_image_1}
                            className="h-full w-full object-cover object-center"
                        />
                    </div>
                </div>

                {/* Product info */}
                <div className="mx-auto max-w-2xl px-4 pb-16 pt-10 sm:px-6 lg:grid lg:max-w-7xl lg:grid-cols-3 lg:grid-rows-[auto,auto,1fr] lg:gap-x-8 lg:px-8 lg:pb-24 lg:pt-16">
                    <div className="lg:col-span-2 lg:border-r lg:border-gray-200 lg:pr-8">
                        <h1 className="text-2xl font-bold tracking-tight text-gray-900 sm:text-3xl">{wear.name}</h1>
                    </div>

                    {/* Options */}
                    <div className="mt-4 lg:row-span-3 lg:mt-0">
                        <h2 className="sr-only">Product information</h2>
                        <p className="text-3xl tracking-tight text-gray-900">{wear.price} р</p>

                        <form className="mt-10">
                            {/* Colors */}
                            <div>
                                <h3 className="text-sm font-medium text-gray-900">Color</h3>

                                <fieldset aria-label="Choose a color" className="mt-4">
                                    <RadioGroup value={selectedColor} onChange={setSelectedColor} className="flex items-center space-x-3">
                                        {product.colors.map((color) => (
                                            <Radio
                                                key={color.name}
                                                value={color}
                                                aria-label={color.name}
                                                className={classNames(
                                                    color.selectedClass,
                                                    'relative -m-0.5 flex cursor-pointer items-center justify-center rounded-full p-0.5 focus:outline-none data-[checked]:ring-2 data-[focus]:data-[checked]:ring data-[focus]:data-[checked]:ring-offset-1',
                                                )}
                                            >
                        <span
                            aria-hidden="true"
                            className={classNames(
                                color.class,
                                'h-8 w-8 rounded-full border border-black border-opacity-10',
                            )}
                        />
                                            </Radio>
                                        ))}
                                    </RadioGroup>
                                </fieldset>
                            </div>

                            {/* Sizes */}
                            <div className="mt-10">
                                <fieldset aria-label="Choose a size" className="mt-4">
                                    <RadioGroup
                                        value={selectedSize}
                                        onChange={setSelectedSize}
                                        className="grid grid-cols-4 gap-4 sm:grid-cols-8 lg:grid-cols-4"
                                    >
                                        {product.sizes.map((size) => (
                                            <Radio
                                                key={size.name}
                                                value={size}
                                                disabled={!size.inStock}
                                                className={classNames(
                                                    size.inStock
                                                        ? 'cursor-pointer bg-white text-gray-900 shadow-sm'
                                                        : 'cursor-not-allowed bg-gray-50 text-gray-200',
                                                    'group relative flex items-center justify-center rounded-md border px-4 py-3 text-sm font-medium uppercase hover:bg-gray-50 focus:outline-none data-[focus]:ring-2 data-[focus]:ring-indigo-500 sm:flex-1 sm:py-6',
                                                )}
                                            >
                                                <span>{size.name}</span>
                                                {size.inStock ? (
                                                    <span
                                                        aria-hidden="true"
                                                        className="pointer-events-none absolute -inset-px rounded-md border-2 border-transparent group-data-[focus]:border group-data-[checked]:border-indigo-500"
                                                    />
                                                ) : (
                                                    <span
                                                        aria-hidden="true"
                                                        className="pointer-events-none absolute -inset-px rounded-md border-2 border-gray-200"
                                                    >
                            <svg
                                stroke="currentColor"
                                viewBox="0 0 100 100"
                                preserveAspectRatio="none"
                                className="absolute inset-0 h-full w-full stroke-2 text-gray-200"
                            >
                              <line x1={0} x2={100} y1={100} y2={0} vectorEffect="non-scaling-stroke" />
                            </svg>
                          </span>
                                                )}
                                            </Radio>
                                        ))}
                                    </RadioGroup>
                                </fieldset>
                            </div>

                            <button
                                type="submit"
                                className="mt-10 flex w-full items-center justify-center rounded-md border border-transparent bg-indigo-600 px-8 py-3 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                            >
                                Добавить в корзину
                            </button>
                        </form>
                    </div>

                    <div className="py-10 lg:col-span-2 lg:col-start-1 lg:border-r lg:border-gray-200 lg:pb-16 lg:pr-8 lg:pt-6">
                        {/* Description and details */}
                        <div>
                            <h3 className="sr-only">Description</h3>

                            <div className="space-y-6">
                                <p className="text-base text-gray-900">{wear.description}</p>
                            </div>
                        </div>

                        <div className="mt-10">
                            <h2 className="text-sm font-medium text-gray-900">Details</h2>

                            <div className="mt-4 space-y-6">
                                <p className="text-sm text-gray-600">{wear.characteristics}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

