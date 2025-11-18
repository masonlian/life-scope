package com.masonlian.panelbackend.request;

import java.math.BigDecimal;
import java.sql.Timestamp;
import java.util.List;

public class LocationData {

    private  BigDecimal latitude;
    private BigDecimal longitude;
    private  String publicName;
    private  Timestamp acquiringTime;
    private String address ;
    private String poi;
    private String placeId ;

    public BigDecimal getLatitude() {
        return latitude;
    }

    public void setLatitude(BigDecimal latitude) {
        this.latitude = latitude;
    }

    public BigDecimal getLongitude() {
        return longitude;
    }

    public void setLongitude(BigDecimal longitude) {
        this.longitude = longitude;
    }

    public String getPublicName() {
        return publicName;
    }

    public void setPublicName(String publicName) {
        this.publicName = publicName;
    }

    public Timestamp getAcquiringTime() {
        return acquiringTime;
    }

    public void setAcquiringTime(Timestamp acquiringTime) {
        this.acquiringTime = acquiringTime;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getPoi() {
        return poi;
    }

    public void setPoi(String poi) {
        this.poi = poi;
    }

    public String getPlaceId() {
        return placeId;
    }

    public void setPlaceId(String placeId) {
        this.placeId = placeId;
    }
}
