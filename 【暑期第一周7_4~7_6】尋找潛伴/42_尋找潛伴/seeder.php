<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\Store;

class PartnerSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        Store::create([
            "partner_id" => "1",
            "group_time" => "08-05",
            "location" => "小琉球",
            "money" => "400",
            "email" => "C1091931100@gmail.com",
            "type" => "浮潛",
            "license" => "無",
            "people_limit" => "8",
            "people_number" => "4",
        ]);

        Store::create([
            "partner_id" => "2",
            "group_time" => "08-10",
            "location" => "綠島",
            "money" => "14000",
            "email" => "C1091931101@gmail.com",
            "type" => "自由潛水",
            "license" => "有",
            "people_limit" => "4",
            "people_number" => "1",
        ]);

        Store::create([
            "partner_id" => "3",
            "group_time" => "08-15",
            "location" => "墾丁",
            "money" => "2500",
            "email" => "C1091931102@gmail.com",
            "type" => "水肺潛水",
            "license" => "無",
            "people_limit" => "8",
            "people_number" => "6",
        ]);

        Store::create([
            "partner_id" => "4",
            "group_time" => "08-20",
            "location" => "小琉球",
            "money" => "400",
            "email" => "C1091931103@gmail.com",
            "type" => "浮潛",
            "license" => "無",
            "people_limit" => "10,
            "people_number" => "2",
        ]);

        Store::create([
            "partner_id" => "5",
            "group_time" => "08-22",
            "location" => "蘭嶼",
            "money" => "12000",
            "email" => "C1091931104@gmail.com",
            "type" => "水肺潛水",
            "license" => "有",
            "people_limit" => "8",
            "people_number" => "5",
        ]);

        Store::create([
            "partner_id" => "6",
            "group_time" => "08-24",
            "location" => "綠島",
            "money" => "400",
            "email" => "C1091931105@gmail.com",
            "type" => "浮潛",
            "license" => "無",
            "people_limit" => "10",
            "people_number" => "4",
        ]);

        Store::create([
            "partner_id" => "7",
            "group_time" => "08-28",
            "location" => "墾丁",
            "money" => "15000",
            "email" => "C1091931106@gmail.com",
            "type" => "自由潛水",
            "license" => "有",
            "people_limit" => "6",
            "people_number" => "3",
        ]);

        Store::create([
            "partner_id" => "8",
            "group_time" => "09-01",
            "location" => "小琉球",
            "money" => "2500",
            "email" => "C1091931107@gmail.com",
            "type" => "水肺潛水",
            "license" => "無",
            "people_limit" => "8",
            "people_number" => "6",
        ]);

        Store::create([
            "partner_id" => "9",
            "group_time" => "09-05",
            "location" => "綠島",
            "money" => "13000",
            "email" => "C1091931108@gmail.com",
            "type" => "自由潛水",
            "license" => "有",
            "people_limit" => "6",
            "people_number" => "4",
        ]);

        Store::create([
            "partner_id" => "10",
            "group_time" => "09-20",
            "location" => "綠島",
            "money" => "400",
            "email" => "C1091931109@gmail.com",
            "type" => "浮潛",
            "license" => "無",
            "people_limit" => "10",
            "people_number" => "2",
        ]);
    }
}
