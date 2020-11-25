let map;

function initMap() {
//   map = new google.maps.Map(document.getElementById("map"), {
//     center: { lat: 50.762031, lng: 16.2870917 },
//     zoom: 14,
//   });
// }

var uluru = {lat: 51.762031, lng: 16.2870917};
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 10, center: uluru});
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({position: uluru, map: map});
}

//
//let map;
//
//function initMap() {
//  map = new google.maps.Map(document.getElementById("map"), {
//    zoom: 16,
//    center: new google.maps.LatLng(-33.91722, 151.23064),
//    mapTypeId: "roadmap",
//  });
//  const iconBase = "/static/";
//  const icons = {
//    parking: {
//      name: "Parking",
//      icon: iconBase + "truck_ico.png",
//    },
//  };
//  const features = [
//    {
//      position: new google.maps.LatLng(-33.91721, 151.2263),
//      type: "parking",
//    },
//    {
//      position: new google.maps.LatLng(-33.91539, 151.2282),
//      type: "parking",
//    },
//    {
//      position: new google.maps.LatLng(-33.91747, 151.22912),
//      type: "parking",
//    },
//    {
//      position: new google.maps.LatLng(-33.9191, 151.22907),
//      type: "parking",
//    },
//    {
//      position: new google.maps.LatLng(-33.91725, 151.23011),
//      type: "parking",
//    },
//
//  ];
//  features.forEach((feature) => {
//    new google.maps.Marker({
//      position: feature.position,
//      icon: icons[feature.type].icon,
//      map: map,
//    });
//  });
//  const legend = document.getElementById("legend");
//
//  for (const key in icons) {
//    const type = icons[key];
//    const name = type.name;
//    const icon = type.icon;
//    const div = document.createElement("div");
//    div.innerHTML = '<img src="' + icon + '"> ' + name;
//    legend.appendChild(div);
//  }
//  map.controls[google.maps.ControlPosition.RIGHT_BOTTOM].push(legend);
//}