"""The Tuya BLE integration."""
from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing_extensions import Final

DOMAIN: Final = "tuya_ble"

DEVICE_METADATA_UUIDS: Final = "uuids"

DEVICE_DEF_MANUFACTURER: Final = "Tuya"
SET_DISCONNECTED_DELAY = 10 * 60

CONF_UUID: Final = "uuid"
CONF_LOCAL_KEY: Final = "local_key"
CONF_CATEGORY: Final = "category"
CONF_PRODUCT_ID: Final = "product_id"
CONF_DEVICE_NAME: Final = "device_name"
CONF_PRODUCT_MODEL: Final = "product_model"
CONF_PRODUCT_NAME: Final = "product_name"

TUYA_API_DEVICES_URL: Final = "/v1.0/users/%s/devices"
TUYA_API_FACTORY_INFO_URL: Final = "/v1.0/iot-03/devices/factory-infos?device_ids=%s"
TUYA_FACTORY_INFO_MAC: Final = "mac"

BATTERY_STATE_LOW: Final = "low"
BATTERY_STATE_NORMAL: Final = "normal"
BATTERY_STATE_HIGH: Final = "high"

BATTERY_NOT_CHARGING: Final = "not_charging"
BATTERY_CHARGING: Final = "charging"
BATTERY_CHARGED: Final = "charged"

CO2_LEVEL_NORMAL: Final = "normal"
CO2_LEVEL_ALARM: Final = "alarm"

FINGERBOT_MODE_PUSH: Final = "push"
FINGERBOT_MODE_SWITCH: Final = "switch"
FINGERBOT_MODE_PROGRAM: Final = "program"
FINGERBOT_BUTTON_EVENT: Final = "fingerbot_button_pressed"

# ---------------------------------------------------------------------------
# Tuya cloud credential / config constants
# (previously imported from homeassistant.components.tuya.const, removed in HA 2026.x)
# ---------------------------------------------------------------------------
CONF_ACCESS_ID: Final = "access_id"
CONF_ACCESS_SECRET: Final = "access_secret"
CONF_APP_TYPE: Final = "tuya_app_type"
CONF_AUTH_TYPE: Final = "auth_type"
CONF_COUNTRY_CODE: Final = "country_code"
CONF_ENDPOINT: Final = "endpoint"
CONF_PASSWORD: Final = "password"
CONF_USERNAME: Final = "username"

TUYA_SMART_APP: Final = "tuyaSmart"
SMARTLIFE_APP: Final = "smartlife"

TUYA_RESPONSE_CODE: Final = "code"
TUYA_RESPONSE_MSG: Final = "msg"
TUYA_RESPONSE_RESULT: Final = "result"
TUYA_RESPONSE_SUCCESS: Final = "success"

TUYA_DOMAIN: Final = "tuya"


@dataclass
class TuyaCountry:
    """Tuya country definition."""

    name: str
    country_code: str
    endpoint: str


TUYA_COUNTRIES: Final = [
    TuyaCountry("Afghanistan", "93", "https://openapi.tuyaeu.com"),
    TuyaCountry("Albania", "355", "https://openapi.tuyaeu.com"),
    TuyaCountry("Algeria", "213", "https://openapi.tuyaeu.com"),
    TuyaCountry("American Samoa", "1-684", "https://openapi.tuyaus.com"),
    TuyaCountry("Andorra", "376", "https://openapi.tuyaeu.com"),
    TuyaCountry("Angola", "244", "https://openapi.tuyaeu.com"),
    TuyaCountry("Anguilla", "1-264", "https://openapi.tuyaus.com"),
    TuyaCountry("Antarctica", "672", "https://openapi.tuyaus.com"),
    TuyaCountry("Antigua and Barbuda", "1-268", "https://openapi.tuyaus.com"),
    TuyaCountry("Argentina", "54", "https://openapi.tuyaus.com"),
    TuyaCountry("Armenia", "374", "https://openapi.tuyaeu.com"),
    TuyaCountry("Aruba", "297", "https://openapi.tuyaus.com"),
    TuyaCountry("Australia", "61", "https://openapi.tuyaeu.com"),
    TuyaCountry("Austria", "43", "https://openapi.tuyaeu.com"),
    TuyaCountry("Azerbaijan", "994", "https://openapi.tuyaeu.com"),
    TuyaCountry("Bahamas", "1-242", "https://openapi.tuyaus.com"),
    TuyaCountry("Bahrain", "973", "https://openapi.tuyaeu.com"),
    TuyaCountry("Bangladesh", "880", "https://openapi.tuyaeu.com"),
    TuyaCountry("Barbados", "1-246", "https://openapi.tuyaus.com"),
    TuyaCountry("Belarus", "375", "https://openapi.tuyaeu.com"),
    TuyaCountry("Belgium", "32", "https://openapi.tuyaeu.com"),
    TuyaCountry("Belize", "501", "https://openapi.tuyaus.com"),
    TuyaCountry("Benin", "229", "https://openapi.tuyaeu.com"),
    TuyaCountry("Bermuda", "1-441", "https://openapi.tuyaus.com"),
    TuyaCountry("Bhutan", "975", "https://openapi.tuyaeu.com"),
    TuyaCountry("Bolivia", "591", "https://openapi.tuyaus.com"),
    TuyaCountry("Bosnia and Herzegovina", "387", "https://openapi.tuyaeu.com"),
    TuyaCountry("Botswana", "267", "https://openapi.tuyaeu.com"),
    TuyaCountry("Brazil", "55", "https://openapi.tuyaus.com"),
    TuyaCountry("British Indian Ocean Territory", "246", "https://openapi.tuyaus.com"),
    TuyaCountry("British Virgin Islands", "1-284", "https://openapi.tuyaus.com"),
    TuyaCountry("Brunei", "673", "https://openapi.tuyaus.com"),
    TuyaCountry("Bulgaria", "359", "https://openapi.tuyaeu.com"),
    TuyaCountry("Burkina Faso", "226", "https://openapi.tuyaeu.com"),
    TuyaCountry("Burundi", "257", "https://openapi.tuyaeu.com"),
    TuyaCountry("Cambodia", "855", "https://openapi.tuyaus.com"),
    TuyaCountry("Cameroon", "237", "https://openapi.tuyaeu.com"),
    TuyaCountry("Canada", "1", "https://openapi.tuyaus.com"),
    TuyaCountry("Cape Verde", "238", "https://openapi.tuyaeu.com"),
    TuyaCountry("Cayman Islands", "1-345", "https://openapi.tuyaus.com"),
    TuyaCountry("Central African Republic", "236", "https://openapi.tuyaeu.com"),
    TuyaCountry("Chad", "235", "https://openapi.tuyaeu.com"),
    TuyaCountry("Chile", "56", "https://openapi.tuyaus.com"),
    TuyaCountry("China", "86", "https://openapi.tuyacn.com"),
    TuyaCountry("Christmas Island", "61", "https://openapi.tuyaus.com"),
    TuyaCountry("Cocos Islands", "61", "https://openapi.tuyaus.com"),
    TuyaCountry("Colombia", "57", "https://openapi.tuyaus.com"),
    TuyaCountry("Comoros", "269", "https://openapi.tuyaeu.com"),
    TuyaCountry("Cook Islands", "682", "https://openapi.tuyaus.com"),
    TuyaCountry("Costa Rica", "506", "https://openapi.tuyaus.com"),
    TuyaCountry("Croatia", "385", "https://openapi.tuyaeu.com"),
    TuyaCountry("Cuba", "53", "https://openapi.tuyaus.com"),
    TuyaCountry("Curacao", "599", "https://openapi.tuyaus.com"),
    TuyaCountry("Cyprus", "357", "https://openapi.tuyaeu.com"),
    TuyaCountry("Czech Republic", "420", "https://openapi.tuyaeu.com"),
    TuyaCountry("Democratic Republic of the Congo", "243", "https://openapi.tuyaeu.com"),
    TuyaCountry("Denmark", "45", "https://openapi.tuyaeu.com"),
    TuyaCountry("Djibouti", "253", "https://openapi.tuyaeu.com"),
    TuyaCountry("Dominica", "1-767", "https://openapi.tuyaus.com"),
    TuyaCountry("Dominican Republic", "1-809", "https://openapi.tuyaus.com"),
    TuyaCountry("East Timor", "670", "https://openapi.tuyaus.com"),
    TuyaCountry("Ecuador", "593", "https://openapi.tuyaus.com"),
    TuyaCountry("Egypt", "20", "https://openapi.tuyaeu.com"),
    TuyaCountry("El Salvador", "503", "https://openapi.tuyaus.com"),
    TuyaCountry("Equatorial Guinea", "240", "https://openapi.tuyaeu.com"),
    TuyaCountry("Eritrea", "291", "https://openapi.tuyaeu.com"),
    TuyaCountry("Estonia", "372", "https://openapi.tuyaeu.com"),
    TuyaCountry("Ethiopia", "251", "https://openapi.tuyaeu.com"),
    TuyaCountry("Falkland Islands", "500", "https://openapi.tuyaus.com"),
    TuyaCountry("Faroe Islands", "298", "https://openapi.tuyaeu.com"),
    TuyaCountry("Fiji", "679", "https://openapi.tuyaus.com"),
    TuyaCountry("Finland", "358", "https://openapi.tuyaeu.com"),
    TuyaCountry("France", "33", "https://openapi.tuyaeu.com"),
    TuyaCountry("French Polynesia", "689", "https://openapi.tuyaus.com"),
    TuyaCountry("Gabon", "241", "https://openapi.tuyaeu.com"),
    TuyaCountry("Gambia", "220", "https://openapi.tuyaeu.com"),
    TuyaCountry("Georgia", "995", "https://openapi.tuyaeu.com"),
    TuyaCountry("Germany", "49", "https://openapi.tuyaeu.com"),
    TuyaCountry("Ghana", "233", "https://openapi.tuyaeu.com"),
    TuyaCountry("Gibraltar", "350", "https://openapi.tuyaeu.com"),
    TuyaCountry("Greece", "30", "https://openapi.tuyaeu.com"),
    TuyaCountry("Greenland", "299", "https://openapi.tuyaeu.com"),
    TuyaCountry("Grenada", "1-473", "https://openapi.tuyaus.com"),
    TuyaCountry("Guam", "1-671", "https://openapi.tuyaus.com"),
    TuyaCountry("Guatemala", "502", "https://openapi.tuyaus.com"),
    TuyaCountry("Guernsey", "44-1481", "https://openapi.tuyaeu.com"),
    TuyaCountry("Guinea", "224", "https://openapi.tuyaeu.com"),
    TuyaCountry("Guinea-Bissau", "245", "https://openapi.tuyaeu.com"),
    TuyaCountry("Guyana", "592", "https://openapi.tuyaus.com"),
    TuyaCountry("Haiti", "509", "https://openapi.tuyaus.com"),
    TuyaCountry("Honduras", "504", "https://openapi.tuyaus.com"),
    TuyaCountry("Hong Kong", "852", "https://openapi.tuyaus.com"),
    TuyaCountry("Hungary", "36", "https://openapi.tuyaeu.com"),
    TuyaCountry("Iceland", "354", "https://openapi.tuyaeu.com"),
    TuyaCountry("India", "91", "https://openapi.tuyain.com"),
    TuyaCountry("Indonesia", "62", "https://openapi.tuyaus.com"),
    TuyaCountry("Iran", "98", "https://openapi.tuyaeu.com"),
    TuyaCountry("Iraq", "964", "https://openapi.tuyaeu.com"),
    TuyaCountry("Ireland", "353", "https://openapi.tuyaeu.com"),
    TuyaCountry("Isle of Man", "44-1624", "https://openapi.tuyaeu.com"),
    TuyaCountry("Israel", "972", "https://openapi.tuyaeu.com"),
    TuyaCountry("Italy", "39", "https://openapi.tuyaeu.com"),
    TuyaCountry("Ivory Coast", "225", "https://openapi.tuyaeu.com"),
    TuyaCountry("Jamaica", "1-876", "https://openapi.tuyaus.com"),
    TuyaCountry("Japan", "81", "https://openapi.tuyaus.com"),
    TuyaCountry("Jersey", "44-1534", "https://openapi.tuyaeu.com"),
    TuyaCountry("Jordan", "962", "https://openapi.tuyaeu.com"),
    TuyaCountry("Kazakhstan", "7", "https://openapi.tuyaeu.com"),
    TuyaCountry("Kenya", "254", "https://openapi.tuyaeu.com"),
    TuyaCountry("Kiribati", "686", "https://openapi.tuyaus.com"),
    TuyaCountry("Kosovo", "383", "https://openapi.tuyaeu.com"),
    TuyaCountry("Kuwait", "965", "https://openapi.tuyaeu.com"),
    TuyaCountry("Kyrgyzstan", "996", "https://openapi.tuyaeu.com"),
    TuyaCountry("Laos", "856", "https://openapi.tuyaus.com"),
    TuyaCountry("Latvia", "371", "https://openapi.tuyaeu.com"),
    TuyaCountry("Lebanon", "961", "https://openapi.tuyaeu.com"),
    TuyaCountry("Lesotho", "266", "https://openapi.tuyaeu.com"),
    TuyaCountry("Liberia", "231", "https://openapi.tuyaeu.com"),
    TuyaCountry("Libya", "218", "https://openapi.tuyaeu.com"),
    TuyaCountry("Liechtenstein", "423", "https://openapi.tuyaeu.com"),
    TuyaCountry("Lithuania", "370", "https://openapi.tuyaeu.com"),
    TuyaCountry("Luxembourg", "352", "https://openapi.tuyaeu.com"),
    TuyaCountry("Macao", "853", "https://openapi.tuyaus.com"),
    TuyaCountry("Macedonia", "389", "https://openapi.tuyaeu.com"),
    TuyaCountry("Madagascar", "261", "https://openapi.tuyaeu.com"),
    TuyaCountry("Malawi", "265", "https://openapi.tuyaeu.com"),
    TuyaCountry("Malaysia", "60", "https://openapi.tuyaus.com"),
    TuyaCountry("Maldives", "960", "https://openapi.tuyaeu.com"),
    TuyaCountry("Mali", "223", "https://openapi.tuyaeu.com"),
    TuyaCountry("Malta", "356", "https://openapi.tuyaeu.com"),
    TuyaCountry("Marshall Islands", "692", "https://openapi.tuyaus.com"),
    TuyaCountry("Mauritania", "222", "https://openapi.tuyaeu.com"),
    TuyaCountry("Mauritius", "230", "https://openapi.tuyaeu.com"),
    TuyaCountry("Mayotte", "262", "https://openapi.tuyaeu.com"),
    TuyaCountry("Mexico", "52", "https://openapi.tuyaus.com"),
    TuyaCountry("Micronesia", "691", "https://openapi.tuyaus.com"),
    TuyaCountry("Moldova", "373", "https://openapi.tuyaeu.com"),
    TuyaCountry("Monaco", "377", "https://openapi.tuyaeu.com"),
    TuyaCountry("Mongolia", "976", "https://openapi.tuyaus.com"),
    TuyaCountry("Montenegro", "382", "https://openapi.tuyaeu.com"),
    TuyaCountry("Montserrat", "1-664", "https://openapi.tuyaus.com"),
    TuyaCountry("Morocco", "212", "https://openapi.tuyaeu.com"),
    TuyaCountry("Mozambique", "258", "https://openapi.tuyaeu.com"),
    TuyaCountry("Myanmar", "95", "https://openapi.tuyaus.com"),
    TuyaCountry("Namibia", "264", "https://openapi.tuyaeu.com"),
    TuyaCountry("Nauru", "674", "https://openapi.tuyaus.com"),
    TuyaCountry("Nepal", "977", "https://openapi.tuyaeu.com"),
    TuyaCountry("Netherlands", "31", "https://openapi.tuyaeu.com"),
    TuyaCountry("Netherlands Antilles", "599", "https://openapi.tuyaus.com"),
    TuyaCountry("New Caledonia", "687", "https://openapi.tuyaus.com"),
    TuyaCountry("New Zealand", "64", "https://openapi.tuyaeu.com"),
    TuyaCountry("Nicaragua", "505", "https://openapi.tuyaus.com"),
    TuyaCountry("Niger", "227", "https://openapi.tuyaeu.com"),
    TuyaCountry("Nigeria", "234", "https://openapi.tuyaeu.com"),
    TuyaCountry("Niue", "683", "https://openapi.tuyaus.com"),
    TuyaCountry("North Korea", "850", "https://openapi.tuyaus.com"),
    TuyaCountry("Northern Mariana Islands", "1-670", "https://openapi.tuyaus.com"),
    TuyaCountry("Norway", "47", "https://openapi.tuyaeu.com"),
    TuyaCountry("Oman", "968", "https://openapi.tuyaeu.com"),
    TuyaCountry("Pakistan", "92", "https://openapi.tuyaeu.com"),
    TuyaCountry("Palau", "680", "https://openapi.tuyaus.com"),
    TuyaCountry("Palestine", "970", "https://openapi.tuyaeu.com"),
    TuyaCountry("Panama", "507", "https://openapi.tuyaus.com"),
    TuyaCountry("Papua New Guinea", "675", "https://openapi.tuyaus.com"),
    TuyaCountry("Paraguay", "595", "https://openapi.tuyaus.com"),
    TuyaCountry("Peru", "51", "https://openapi.tuyaus.com"),
    TuyaCountry("Philippines", "63", "https://openapi.tuyaus.com"),
    TuyaCountry("Pitcairn", "64", "https://openapi.tuyaus.com"),
    TuyaCountry("Poland", "48", "https://openapi.tuyaeu.com"),
    TuyaCountry("Portugal", "351", "https://openapi.tuyaeu.com"),
    TuyaCountry("Puerto Rico", "1-787", "https://openapi.tuyaus.com"),
    TuyaCountry("Qatar", "974", "https://openapi.tuyaeu.com"),
    TuyaCountry("Republic of the Congo", "242", "https://openapi.tuyaeu.com"),
    TuyaCountry("Reunion", "262", "https://openapi.tuyaeu.com"),
    TuyaCountry("Romania", "40", "https://openapi.tuyaeu.com"),
    TuyaCountry("Russia", "7", "https://openapi.tuyaeu.com"),
    TuyaCountry("Rwanda", "250", "https://openapi.tuyaeu.com"),
    TuyaCountry("Saint Barthelemy", "590", "https://openapi.tuyaus.com"),
    TuyaCountry("Saint Helena", "290", "https://openapi.tuyaeu.com"),
    TuyaCountry("Saint Kitts and Nevis", "1-869", "https://openapi.tuyaus.com"),
    TuyaCountry("Saint Lucia", "1-758", "https://openapi.tuyaus.com"),
    TuyaCountry("Saint Martin", "590", "https://openapi.tuyaus.com"),
    TuyaCountry("Saint Pierre and Miquelon", "508", "https://openapi.tuyaus.com"),
    TuyaCountry("Saint Vincent and the Grenadines", "1-784", "https://openapi.tuyaus.com"),
    TuyaCountry("Samoa", "685", "https://openapi.tuyaus.com"),
    TuyaCountry("San Marino", "378", "https://openapi.tuyaeu.com"),
    TuyaCountry("Sao Tome and Principe", "239", "https://openapi.tuyaeu.com"),
    TuyaCountry("Saudi Arabia", "966", "https://openapi.tuyaeu.com"),
    TuyaCountry("Senegal", "221", "https://openapi.tuyaeu.com"),
    TuyaCountry("Serbia", "381", "https://openapi.tuyaeu.com"),
    TuyaCountry("Seychelles", "248", "https://openapi.tuyaeu.com"),
    TuyaCountry("Sierra Leone", "232", "https://openapi.tuyaeu.com"),
    TuyaCountry("Singapore", "65", "https://openapi.tuyaus.com"),
    TuyaCountry("Sint Maarten", "1-721", "https://openapi.tuyaus.com"),
    TuyaCountry("Slovakia", "421", "https://openapi.tuyaeu.com"),
    TuyaCountry("Slovenia", "386", "https://openapi.tuyaeu.com"),
    TuyaCountry("Solomon Islands", "677", "https://openapi.tuyaus.com"),
    TuyaCountry("Somalia", "252", "https://openapi.tuyaeu.com"),
    TuyaCountry("South Africa", "27", "https://openapi.tuyaeu.com"),
    TuyaCountry("South Korea", "82", "https://openapi.tuyaus.com"),
    TuyaCountry("South Sudan", "211", "https://openapi.tuyaeu.com"),
    TuyaCountry("Spain", "34", "https://openapi.tuyaeu.com"),
    TuyaCountry("Sri Lanka", "94", "https://openapi.tuyaeu.com"),
    TuyaCountry("Sudan", "249", "https://openapi.tuyaeu.com"),
    TuyaCountry("Suriname", "597", "https://openapi.tuyaus.com"),
    TuyaCountry("Svalbard and Jan Mayen", "47", "https://openapi.tuyaeu.com"),
    TuyaCountry("Swaziland", "268", "https://openapi.tuyaeu.com"),
    TuyaCountry("Sweden", "46", "https://openapi.tuyaeu.com"),
    TuyaCountry("Switzerland", "41", "https://openapi.tuyaeu.com"),
    TuyaCountry("Syria", "963", "https://openapi.tuyaeu.com"),
    TuyaCountry("Taiwan", "886", "https://openapi.tuyaus.com"),
    TuyaCountry("Tajikistan", "992", "https://openapi.tuyaeu.com"),
    TuyaCountry("Tanzania", "255", "https://openapi.tuyaeu.com"),
    TuyaCountry("Thailand", "66", "https://openapi.tuyaus.com"),
    TuyaCountry("Togo", "228", "https://openapi.tuyaeu.com"),
    TuyaCountry("Tokelau", "690", "https://openapi.tuyaus.com"),
    TuyaCountry("Tonga", "676", "https://openapi.tuyaus.com"),
    TuyaCountry("Trinidad and Tobago", "1-868", "https://openapi.tuyaus.com"),
    TuyaCountry("Tunisia", "216", "https://openapi.tuyaeu.com"),
    TuyaCountry("Turkey", "90", "https://openapi.tuyaeu.com"),
    TuyaCountry("Turkmenistan", "993", "https://openapi.tuyaeu.com"),
    TuyaCountry("Turks and Caicos Islands", "1-649", "https://openapi.tuyaus.com"),
    TuyaCountry("Tuvalu", "688", "https://openapi.tuyaus.com"),
    TuyaCountry("U.S. Virgin Islands", "1-340", "https://openapi.tuyaus.com"),
    TuyaCountry("Uganda", "256", "https://openapi.tuyaeu.com"),
    TuyaCountry("Ukraine", "380", "https://openapi.tuyaeu.com"),
    TuyaCountry("United Arab Emirates", "971", "https://openapi.tuyaeu.com"),
    TuyaCountry("United Kingdom", "44", "https://openapi.tuyaeu.com"),
    TuyaCountry("United States", "1", "https://openapi.tuyaus.com"),
    TuyaCountry("Uruguay", "598", "https://openapi.tuyaus.com"),
    TuyaCountry("Uzbekistan", "998", "https://openapi.tuyaeu.com"),
    TuyaCountry("Vanuatu", "678", "https://openapi.tuyaus.com"),
    TuyaCountry("Vatican", "379", "https://openapi.tuyaeu.com"),
    TuyaCountry("Venezuela", "58", "https://openapi.tuyaus.com"),
    TuyaCountry("Vietnam", "84", "https://openapi.tuyaus.com"),
    TuyaCountry("Wallis and Futuna", "681", "https://openapi.tuyaus.com"),
    TuyaCountry("Western Sahara", "212", "https://openapi.tuyaeu.com"),
    TuyaCountry("Yemen", "967", "https://openapi.tuyaeu.com"),
    TuyaCountry("Zambia", "260", "https://openapi.tuyaeu.com"),
    TuyaCountry("Zimbabwe", "263", "https://openapi.tuyaeu.com"),
]

