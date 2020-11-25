//let map;
//
//function initMap() {
////   map = new google.maps.Map(document.getElementById("map"), {
////     center: { lat: 50.762031, lng: 16.2870917 },
////     zoom: 14,
////   });
//// }
//
//var uluru = {lat: 51.762031, lng: 16.2870917};
//  // The map, centered at Uluru
//  var map = new google.maps.Map(
//      document.getElementById('map'), {zoom: 10, center: uluru});
//  // The marker, positioned at Uluru
//  var marker = new google.maps.Marker({position: uluru, map: map});
//}


let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 7,
    center: new google.maps.LatLng(51.962031, 18.2870917),
    mapTypeId: "roadmap",
  });
  const iconBase = "/static/";
  const icons = {
    parking: {
      name: "Parking",
      icon: iconBase + "truck_ico.png",
    },
  };
  const features = [
    {
      position: new google.maps.LatLng(51.59147729330014, 18.86946112504381),
      type: "parking",
    },
    {
      position: new google.maps.LatLng(50.84061407973195, 17.48603277330002),
      type: "parking",
    },
    {
      position: new google.maps.LatLng(52.067228444873194, 18.14936855403365),
      type: "parking",
    },
    {
      position: new google.maps.LatLng(51.96209951349473, 19.836820887080826),
      type: "parking",
    },
    {
      position: new google.maps.LatLng(51.003466921328375, 17.201955016386837),
      type: "parking",
    },

  ];
  features.forEach((feature) => {
    new google.maps.Marker({
      position: feature.position,
      icon: icons[feature.type].icon,
      map: map,
    });
  });
  const legend = document.getElementById("legend");

  for (const key in icons) {
    const type = icons[key];
    const name = type.name;
    const icon = type.icon;
    const div = document.createElement("div");
    div.innerHTML = '<img src="' + icon + '"> ' + name;
    legend.appendChild(div);
  }
  map.controls[google.maps.ControlPosition.RIGHT_BOTTOM].push(legend);
}