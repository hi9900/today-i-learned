package com.example.googlemaptest

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.google.android.gms.maps.CameraUpdateFactory
import com.google.android.gms.maps.GoogleMap
import com.google.android.gms.maps.OnMapReadyCallback
import com.google.android.gms.maps.SupportMapFragment
import com.google.android.gms.maps.model.LatLng
import com.google.android.gms.maps.model.MarkerOptions

class MainActivity : AppCompatActivity(), OnMapReadyCallback {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val mapFragment = supportFragmentManager.findFragmentById(R.id.map) as? SupportMapFragment
        mapFragment?.getMapAsync(this)
    }

    override fun onMapReady(googleMap: GoogleMap) {
        val multicampus = LatLng(37.5013068, 127.0385654)
        googleMap.addMarker(
            MarkerOptions()
                .position(multicampus)
                .title("역삼 멀티캠퍼스")
        )

        val starbugs = LatLng(37.501903, 127.039468)
        googleMap.addMarker(
            MarkerOptions()
                .position(starbugs)
                .title("역삼 스타벅스")
        )

        val kfc = LatLng(37.501954, 127.036129)
        googleMap.addMarker(
            MarkerOptions()
                .position(kfc)
                .title("역삼 kfc")
        )

        val cu = LatLng(37.501426, 127.040120)
        googleMap.addMarker(
            MarkerOptions()
                .position(cu)
                .title("CU")
        )

        val koreaBank = LatLng(37.500651, 127.038157)
        googleMap.addMarker(
            MarkerOptions()
                .position(koreaBank)
                .title("한국은행")
        )

        googleMap.moveCamera(CameraUpdateFactory.newLatLngZoom(multicampus, 15F))
    }
}